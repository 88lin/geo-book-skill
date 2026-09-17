#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""geo-book-skill 一致性校验。

检查项：
  1. SKILL.md frontmatter 合规（name 与目录同名、description 长度）
  2. 13 张能力卡的六段结构（R / I / A1 / A2 / E / B + 相关能力）完整
  3. 四方一致：SKILL.md 路由表 ↔ capability-index.md ↔ cheatsheet.md ↔ verified.yaml ↔ 磁盘文件
  4. verified.yaml 里的 card / resources 路径真实存在，also_read 指向已存在的 slug
  5. 全仓 markdown 相对链接可解析
  6. resources/ 下 JSON 可解析
  7. AGENTS.md 与 prompts/ 引用的路径存在
  8. 无遗留的编译产物路径（dist/）与断裂的「补充N」编号

用法：python scripts/validate.py    退出码非 0 表示有 error。
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_DIR = os.path.join(ROOT, "geo-playbook")
CAP_DIR = os.path.join(SKILL_DIR, "references", "capabilities")

# Windows 控制台默认 GBK，中文报错会变乱码
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def read(path):
    return io.open(path, encoding="utf-8").read()


def rel(path):
    return os.path.relpath(path, ROOT).replace("\\", "/")


# ── 1. SKILL.md frontmatter ────────────────────────────────────────────────
skill_md = os.path.join(SKILL_DIR, "SKILL.md")
if not os.path.exists(skill_md):
    err("SKILL.md 不存在：%s" % rel(skill_md))
    print("FATAL"), sys.exit(1)

skill_text = read(skill_md)
m = re.match(r"^---\n(.*?)\n---\n", skill_text, re.S)
if not m:
    err("SKILL.md 缺少 YAML frontmatter")
    fm = {}
else:
    try:
        import yaml
        fm = yaml.safe_load(m.group(1)) or {}
    except ImportError:
        warn("未安装 PyYAML，跳过 frontmatter 深度校验（pip install pyyaml）")
        fm = {}
    except Exception as e:
        err("SKILL.md frontmatter 不是合法 YAML：%s" % e)
        fm = {}

if fm:
    if fm.get("name") != os.path.basename(SKILL_DIR):
        err("SKILL.md 的 name=%r 与技能目录名 %r 不一致"
            % (fm.get("name"), os.path.basename(SKILL_DIR)))
    desc = fm.get("description") or ""
    if not desc:
        err("SKILL.md 缺少 description")
    elif len(desc) > 1024:
        err("SKILL.md description 长度 %d 超过 1024 字符上限" % len(desc))

# ── 2/3. 能力卡结构与四方一致 ──────────────────────────────────────────────
REQUIRED_SECTIONS = ["## R — 原文", "## I — 解释", "## A2 — 未来触发",
                     "## E — 执行步骤", "## B — 边界", "## 相关能力"]

disk_slugs = sorted(
    f[:-3] for f in os.listdir(CAP_DIR) if f.endswith(".md")
)

for slug in disk_slugs:
    text = read(os.path.join(CAP_DIR, slug + ".md"))
    for sec in REQUIRED_SECTIONS:
        if sec not in text:
            err("能力卡 %s 缺少段落 %r" % (slug, sec))
    if "## A1 —" not in text:
        err("能力卡 %s 缺少段落 '## A1 —'" % slug)
    # 断裂的补充编号：规范写法是「**补充 · 标题**（来源）」
    for bad in re.findall(r"\*\*补充[一二三四五六七八九十\d]", text):
        err("能力卡 %s 仍使用编号式补充块 %r，应改为「**补充 · 标题**（来源）」" % (slug, bad))

# SKILL.md 路由表里出现的 slug
routed = set(re.findall(r"\| ([a-z][a-z0-9-]+) \|", skill_text))
routed |= set(re.findall(r"^\| [^|]+ \| ([a-z][a-z0-9-]+) \|", skill_text, re.M))
routed = {s for s in routed if s in disk_slugs}

missing_route = sorted(set(disk_slugs) - routed)
if missing_route:
    err("SKILL.md 路由表未覆盖能力卡：%s" % ", ".join(missing_route))

# capability-index.md
idx_path = os.path.join(SKILL_DIR, "references", "capability-index.md")
idx_slugs = set()
if os.path.exists(idx_path):
    idx_slugs = set(re.findall(r"capabilities/([a-z0-9-]+)\.md", read(idx_path)))
    if idx_slugs != set(disk_slugs):
        err("capability-index.md 与磁盘能力卡不一致：仅索引有 %s；仅磁盘有 %s"
            % (sorted(idx_slugs - set(disk_slugs)) or "-",
               sorted(set(disk_slugs) - idx_slugs) or "-"))
else:
    err("缺少 capability-index.md")

# cheatsheet 覆盖度（按标题匹配，只告警）
cheat_path = os.path.join(SKILL_DIR, "references", "cheatsheet.md")
if os.path.exists(cheat_path):
    cheat = read(cheat_path)
    for slug in disk_slugs:
        title = read(os.path.join(CAP_DIR, slug + ".md")).split("\n")[0].lstrip("# ").strip()
        parts = [p.strip() for p in re.split(r"[（：(]", title) if len(p.strip()) >= 3]
        if parts and not any(p in cheat for p in parts):
            warn("cheatsheet.md 未收录能力 %s（%s）" % (slug, title))
else:
    err("缺少 cheatsheet.md")

# ── 4. verified.yaml ───────────────────────────────────────────────────────
vy_path = os.path.join(ROOT, "bundle", "verified.yaml")
if os.path.exists(vy_path):
    try:
        import yaml
        vy = yaml.safe_load(read(vy_path))
    except ImportError:
        vy = None
    except Exception as e:
        err("bundle/verified.yaml 不是合法 YAML：%s" % e)
        vy = None

    if vy:
        caps = vy.get("capabilities", [])
        vy_slugs = sorted(c.get("slug") for c in caps)
        if vy_slugs != disk_slugs:
            err("verified.yaml 与磁盘能力卡不一致：仅登记表有 %s；仅磁盘有 %s"
                % (sorted(set(vy_slugs) - set(disk_slugs)) or "-",
                   sorted(set(disk_slugs) - set(vy_slugs)) or "-"))
        for c in caps:
            slug = c.get("slug")
            base = os.path.dirname(vy_path)
            card = c.get("card", "")
            if not os.path.exists(os.path.join(base, card)):
                err("verified.yaml[%s].card 指向不存在的文件：%s" % (slug, card))
            elif os.path.basename(card) != slug + ".md":
                err("verified.yaml[%s].card 文件名与 slug 不符：%s" % (slug, card))
            for r in c.get("resources", []) or []:
                if not os.path.exists(os.path.join(base, r)):
                    err("verified.yaml[%s].resources 指向不存在的文件：%s" % (slug, r))
            for a in c.get("also_read", []) or []:
                if a not in disk_slugs:
                    err("verified.yaml[%s].also_read 指向未知 slug：%s" % (slug, a))
else:
    err("缺少 bundle/verified.yaml")

# ── 5. 全仓 markdown 相对链接 ──────────────────────────────────────────────
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules")]
    for fn in filenames:
        if not fn.endswith(".md"):
            continue
        path = os.path.join(dirpath, fn)
        for link in LINK_RE.findall(read(path)):
            link = link.split("#")[0].split(" ")[0].strip()
            if not link or link.startswith(("http://", "https://", "mailto:", "#", "<")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(dirpath, link))):
                err("%s 的相对链接失效：%s" % (rel(path), link))

# ── 5b. 技能内的裸路径引用（反引号包裹），必须能从所在文件打开 ───────────────
# markdown 链接之外，卡片与模板里大量用 `references/capabilities/x.md` 这类写法引路，
# agent 会按它去开文件——写错了校验器看不见，所以单独查一遍。
BARE_RE = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|json|txt|template))`")
for dirpath, dirnames, filenames in os.walk(SKILL_DIR):
    dirnames[:] = [d for d in dirnames if d != ".git"]
    for fn in filenames:
        if not fn.endswith(".md"):
            continue
        path = os.path.join(dirpath, fn)
        for raw in sorted(set(BARE_RE.findall(read(path)))):
            if raw.startswith("/") or "://" in raw:
                continue  # 站点根路径（如 /llms.txt）或 URL，不是仓库文件
            if not os.path.exists(os.path.normpath(os.path.join(dirpath, raw))):
                err("%s 的裸路径引用从该文件打不开：`%s`" % (rel(path), raw))

# ── 6. resources JSON ──────────────────────────────────────────────────────
res_dir = os.path.join(SKILL_DIR, "resources")
for fn in sorted(os.listdir(res_dir)):
    if fn.endswith(".json"):
        try:
            obj = json.load(io.open(os.path.join(res_dir, fn), encoding="utf-8"))
        except Exception as e:
            err("resources/%s 不是合法 JSON：%s" % (fn, e))
            continue
        if obj.get("@context") != "https://schema.org":
            err("resources/%s 缺少或写错 @context" % fn)
        if "@type" not in obj:
            err("resources/%s 缺少 @type" % fn)

# ── 7. AGENTS.md / prompts 引用的路径 ──────────────────────────────────────
for doc in ("AGENTS.md", os.path.join("prompts", "geo-playbook.prompt.md")):
    p = os.path.join(ROOT, doc)
    if not os.path.exists(p):
        err("缺少 %s" % doc)
        continue
    for ref in re.findall(r"`(geo-playbook/[^`]+)`", read(p)):
        if not os.path.exists(os.path.join(ROOT, ref)):
            err("%s 引用了不存在的路径：%s" % (doc, ref))

# ── 8. 遗留编译产物路径 ────────────────────────────────────────────────────
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules")]
    for fn in filenames:
        if not fn.endswith((".md", ".yaml")):
            continue
        path = os.path.join(dirpath, fn)
        if rel(path).startswith(("docs/candidates/", "docs/rejected/", "docs/PIPELINE_STATE",
                                 "docs/references.md", "docs/test-results.md", "CHANGELOG.md")):
            continue  # 审计轨迹保留历史路径，不校验
        if "dist/geo-book-skill" in read(path):
            err("%s 残留编译产物路径 dist/geo-book-skill" % rel(path))

# ── 汇总 ───────────────────────────────────────────────────────────────────
for w in warnings:
    print("WARN  %s" % w)
for e in errors:
    print("ERROR %s" % e)

print("")
print("能力卡 %d 张 | resources %d 个 | warnings %d | errors %d"
      % (len(disk_slugs),
         sum(1 for _, _, fs in os.walk(res_dir) for f in fs),
         len(warnings), len(errors)))
sys.exit(1 if errors else 0)
