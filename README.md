<div align="center">

# geo-book-skill

**从《从 SEO 到 GEO》蒸馏的可执行 Agent Skill —— 13 张方法论能力卡，让 AI 助手按实测打法回答 AI 搜索优化问题**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Format](https://img.shields.io/badge/format-Agent_Skills_(SKILL.md)-blueviolet)](geo-playbook/SKILL.md)
[![Capabilities](https://img.shields.io/badge/能力卡-13张-181825)](#-13-张能力卡)
[![Tests](https://img.shields.io/badge/测试-触发31%2F31·评测32%2F32-success)](#-质量与测试)
[![Origin](https://img.shields.io/badge/原书-JingHao‑Leon/geo--book-orange)](https://github.com/JingHao-Leon/geo-book)

**适配：Claude Code · ZCode · WorkBuddy · CodeBuddy · Codex · Cursor · 任意自定义指令 Agent**

[快速开始](#-快速开始) · [使用教程](docs/tutorials/01-快速上手.md) · [能力卡总表](#-13-张能力卡) · [精华长文](docs/DIGEST.md) · [FAQ](#-faq)

</div>

---

## 🤔 这是什么？有什么用？

越来越多的用户买东西前直接问 AI："有哪些好用的 XX""X 和 Y 哪个""X 是不是智商税"。**AI 只给一个答案，你的品牌要么在这个答案里，要么就不存在**——让 AI 在回答里提到你、正面提到你、优先提到你，就是 GEO（生成式引擎优化，不是地理信息）。

市面上的 GEO 资料要么是二手概念翻译，要么是"交给我们做"的服务商软文。这个仓库是第三种东西：**把一本基于六引擎实测的书，蒸馏成 AI 助手能直接执行的方法论技能**。装好后你的 agent 会这样回答问题：

| 你问 | 没装这个技能 | 装了这个技能 |
|---|---|---|
| "内容该发到哪些平台？" | "全平台都重要，要坚持输出" | 反问决策人画像 → 按"定引擎→看生态→按题型→定形态"四步给出引擎×渠道×形态分工表，并给出官网仅占引用 1.37% 的实测依据 |
| "为什么 AI 从来不引用我的文章？" | "内容要优质、坚持原创…" | 四条硬指标 + 七个结构信号逐项体检（pass/fail 附证据行），产出改写稿 |
| "要不要把 AI 爬虫全禁掉？" | 给一段 robots.txt 配置 | 按训练/检索/用户触发三类分别决策，明确拒绝"全部 Disallow"（屏蔽检索类=立即失去被引机会） |

**给谁用**：做内容营销/增长的人、想把官网改成"AI 能用"的 B 端团队、本地门店、给客户做 GEO 服务的乙方、研究 GEO 方法论的 agent 开发者。

## ✨ 五个装它的理由

- **不是金句集，是可执行方法**：每张卡都有触发场景、执行步骤与输入/输出契约、边界与反例——agent 知道什么时候用、怎么算做完、什么时候该停下来问你。
- **一手实测打底**：原书 2026-08-05 对豆包/DeepSeek/腾讯元宝/通义千问/文心一言/Kimi 六引擎做了 12 题 × 6 引擎实测 + 97 次多次采样，每条建议都能追到实测数字。
- **三源交叉印证**：原书（MIT）+ GEO Wiki 百科（CC BY 4.0）+ GeoLook CN-GEO 数据集 187,818 条引用实算（MIT），卡内逐条标注来源与口径。
- **守红线的 agent**：刷好评、编数据、伪装中立洗地、高频批量抓取会被明确拒绝并给合规替代——"铺出来的东西经不起查，上榜就是上榜示众"。
- **经过测试**：触发盲测、跨技能诱饵、32 个真实任务输出评测全通过（见下文质量一节）。

## 🚀 快速开始

### 安装矩阵（按你的 Agent 对号入座）

| Agent | 方式 | 说明 |
|---|---|---|
| **Claude Code** | `cp -r geo-playbook ~/.claude/skills/` | 重开会话自动发现 |
| **ZCode** | `cp -r geo-playbook ~/.zcode/skills/` | 同上 |
| **WorkBuddy / CodeBuddy** 等遵循 Agent Skills 规范的产品 | 把 `geo-playbook/` 目录（含 SKILL.md）放入各自技能目录，或在"技能管理"中导入 | SKILL.md 是通用规范 |
| **Codex / Cursor** 等读取 AGENTS.md 的产品 | 把 [`AGENTS.md`](AGENTS.md) 内容放入 `~/.codex/AGENTS.md`（全局）或项目根目录，路径指向本仓库 | AGENTS.md 内含完整路由表与硬性纪律 |
| **任何支持自定义指令的 AI 产品** | 把 [`prompts/geo-playbook.prompt.md`](prompts/geo-playbook.prompt.md) 全文粘贴进"自定义指令/系统提示" | 单文件压缩版，开箱即用 |

```bash
git clone https://github.com/88lin/geo-book-skill.git
cd geo-book-skill
# Claude Code 示例
mkdir -p ~/.claude/skills && cp -r geo-playbook ~/.claude/skills/
```

### 第一次对话（验证装好了）

```text
我们是做仓储管理系统的，内容应该先发到哪些平台？
```
```text
我写了篇文章结论埋在第三段，帮我改得更容易被 AI 引用
```
```text
我们要不要屏蔽 GPTBot？
```

三条分别应触发：渠道决策树（会先反问决策人画像）、硬指标体检（逐项 pass/fail）、AI 爬虫三类决策（明确警告"全部禁掉"是代价最高反模式）。详细验证与排查见 [教程 01](docs/tutorials/01-快速上手.md)。

## 📚 使用教程

| 教程 | 内容 | 适合 |
|---|---|---|
| [01 · 快速上手](docs/tutorials/01-快速上手.md) | 5 分钟安装、3 个验证 prompt、路由逻辑、没触发怎么办 | 所有人，先读这篇 |
| [02 · 七个实战场景](docs/tutorials/02-场景教程.md) | 渠道决策 / 对比稿 / 旧稿体检 / 一稿多发 / 监测算账 / 负面应对 / AI 爬虫——每个场景给"你说什么→agent 怎么走→得到什么→避坑" | 日常使用者 |
| [03 · 进阶](docs/tutorials/03-进阶.md) | 先测后投实测规程、判停点哲学、归因三段算账、配合 GeoLook 跑自动化、数据保鲜 | 操盘手/乙方 |
| [DIGEST 精华长文](docs/DIGEST.md) | 约 9000 字读懂全书方法论（含陷阱与作者局限） | 不装技能先看原理的人 |

## 🗂 13 张能力卡

| # | 能力卡 | 一句话 | 数据来源 |
|---|---|---|---|
| 1 | geo-channel-map | 四步渠道决策树 + 六引擎信源画像（含官网 1.37% 定律、生态集中度） | 原书 ch6/7/9 + GeoLook |
| 2 | golden-question-formulas | 症状/对比/信任三类黄金问题的内容公式 | 原书 ch8 |
| 3 | citable-content-spec | 可引用四硬指标 + 七结构信号体检改写 | 原书 ch10 + GEO Wiki |
| 4 | geo-query-research | 真实语料捞词 + easy_win/target/skip 三维分级 | 原书 ch10 |
| 5 | one-fish-multi-platform | 一鱼多吃：知乎/公众号/头条三版 + 官网事实页，改写非复制 | 原书 ch10 |
| 6 | geo-monitoring-iteration | 两周周期三分支迭代 + 引用≠提及≠链接 + 归因三段 | 原书 ch10 + GeoLook |
| 7 | geo-test-protocol | 实测规程（新对话/逐字/二值口径）+ 先测后投 + 限速红线 | 原书 ch6/9 |
| 8 | negative-semantic-occupy | "智商税"类负面 query 抢阅卷权：分人群给结论 | 原书 ch9 |
| 9 | lso-local-playbook | 本地商户五步执行（NAP/评价/本地内容） | 原书 ch2 |
| 10 | vso-video-optimization | 视频搜索四件套 + 视频/图文双吃分工 | 原书 ch3 |
| 11 | aeo-answer-optimization | AEO 三板斧 + 答案位占位五步 | 原书 ch4 |
| 12 | brand-data-infrastructure | 数据基建三层；官网=事实源非引用源 | 原书 ch11 + GeoLook |
| 13 | ai-crawler-access | AI 爬虫三类放行策略 + llms.txt + 抓不到排查 | **GEO Wiki + GeoLook**（补充） |

## 🧪 质量与测试

蒸馏流程：整书理解 → 五路并行提取（219 条候选）→ 三重验证（来源/可执行/任务增益）→ 晋级门 → RIA 能力卡 → 压力测试 → 编译交付。全审计轨迹在 [`docs/`](docs/)。

| 测试 | 结果 |
|---|---|
| 触发盲测（独立 agent、含跨技能诱饵，首版） | 31/31 |
| 路由可达性（router 卡） | 5/5 |
| 实际任务输出评测（首版 12 能力 × 正常+边界） | 24/24 |
| v0.2.0 回归（新增 AI 爬虫卡） | 触发 15/15、输出 6/6（含拒绝"全部 Disallow"反模式） |
| v0.3.0 回归（合入 GeoLook 数据） | 输出 2/2 |
| 产物格式校验 `validate_skill_pack` | 0 errors |

亮点场景：agent 会**拒绝**"刷一百条五星好评""1 小时连问 500 次采样""装中立用户洗地""AI 爬虫全部 Disallow"，并给出合规替代方案——边界是功能，不是摆设。

## ⚠️ 数据边界与红线（请务必读）

- **快照时效**：引擎信源数字来自 2026-08-05 单日单账号实测；GeoLook 数据集为 2026-07-14。所有数字按**方向性**使用，不做精确百分比比较；引擎行为随时漂移，技能内置"重要决策前先复测"纪律。
- **行业覆盖**：原书实测覆盖广告电商与教育两行业；其他行业的"决策人-引擎"映射是外推，技能会要求先小样本实测再定渠道。
- **转化归因**：原书未提供"被引用→生意结果"的 ROI 数据（技能提供可测的三段归因方法，但不承诺结果）。
- **永不承诺**：GEO 提高被引用概率，不是保证；任何引擎不欠你一个引用位。
- **技能会拒绝**：刷量刷评、编造数据、伪造评价、批量账号自问自答、伪装中立洗地、高频自动化抓取（约 30 次连续提问触发 DeepSeek 风控）。

## 🧩 来源与配套

| 项目 | 关系 | 许可 |
|---|---|---|
| [JingHao-Leon/geo-book](https://github.com/JingHao-Leon/geo-book) | 原书《从 SEO 到 GEO》——方法论主源 | MIT |
| [GEO Wiki](https://geo.wiki/zh) | 百科补充：AI 爬虫/llms.txt/可引用性七信号/答案循环/十项 KPI | CC BY 4.0 |
| [aigclink/geolook](https://github.com/aigclink/geolook) | **配套技能**（自托管 GEO 流水线：体检/采样/工单/验收）+ CN-GEO 数据集大样本 | MIT |
| [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | **配套技能**（海外引擎向：GEO Score 六维审计、品牌权威扫描、乙方交付流）+ Schema JSON 模板 | MIT |

分工：**geo-playbook 出方法论与决策（为什么、怎么选、怎么写），GeoLook 跑自动化流水线（诊断、采样、验收、交付）**，可同时安装、触发场景基本不重叠。

## 📦 目录结构

```text
geo-playbook/          # 安装这个：Agent Skill（SKILL.md + 13 能力卡 + 速查/术语/概览）
AGENTS.md              # Codex / Cursor 等的通用入口（含完整路由表与硬性纪律）
prompts/               # 纯提示词版：粘贴进任意"自定义指令"即用
bundle/                # Capability Bundle 事实源（verified.yaml + 13 张 RIA 卡），可重新编译
docs/
  tutorials/           # 三篇使用教程（快速上手 / 实战场景 / 进阶）
  DIGEST.md            # 精华长文（约 9000 字）
  BOOK_OVERVIEW.md     # 阶段 0：整书理解（骨架/术语/批判/15 项关键任务）
  verified.md          # 三重验证记录；coverage-audit.md 覆盖审计
  test-results.md      # 全部测试结果与局限声明
  candidates/ rejected/ acceptance/   # 审计轨迹（原始候选/去重/评测用例）
CHANGELOG.md           # 版本历史
```

## ❓ FAQ

<details>
<summary><b>和直接问 ChatGPT "怎么做 GEO" 有什么区别？</b></summary>
通用模型没有实测数据底座，容易给出"内容要优质"式的正确废话，还会把过时的渠道结论（如"知乎是主阵地"——实测已被推翻）当成事实。本技能的每条建议绑定实测依据与反例边界：它知道"豆包对症状型口语题倾向不联网（0/4）"，会劝你别把宝押在视频上；它知道"官网只占引用 1.37%"，会拦下"把预算全砸官网改版"的决策。
</details>

<details>
<summary><b>和 GeoLook 是什么关系？会冲突吗？</b></summary>
互补，可同时安装。geo-playbook 是方法论卡（决策与内容），GeoLook 是自动化流水线（诊断/采样/验收/交付工具）。触发场景基本不重叠：问"怎么选怎么写"走前者，说"给我跑一次诊断"走后者。
</details>

<details>
<summary><b>装了没触发怎么办？</b></summary>
① 确认技能目录位置正确、重开会话；② 问题里带意图关键词（发哪里/怎么写才被引用/监测/智商税/llms.txt）；③ 直接点名能力卡："用 geo-channel-map 帮我分析"。
</details>

<details>
<summary><b>数字过期了怎么办？</b></summary>
技能内置"方向性使用 + 定期复核"纪律。重要决策前用 geo-test-protocol 的规程复测当前引擎行为；复合策略是把资源投向跨期稳定的事实资产（结论前置、对比表、带日期的可验证数据）。
</details>

<details>
<summary><b>能自己改/加能力卡吗？</b></summary>
能。<code>bundle/</code> 是事实源（能力卡 + verified.yaml 登记表）；直接改 <code>geo-playbook/references/capabilities/</code> 下的卡片也行——注意保持六段结构（R/I/A1/A2/E/B）并同步登记表，改动建议走 PR 以便回归测试。
</details>

<details>
<summary><b>WorkBuddy / CodeBuddy 怎么装？</b></summary>
它们与 Claude Code 一样遵循 Agent Skills 规范（SKILL.md 目录）：把 <code>geo-playbook/</code> 目录放到其技能目录，或在技能管理界面导入；部分产品的技能可由 AI 自动生成，直接把本仓库 SKILL.md 内容发给它即可。
</details>

## 📄 License

MIT。原书与实测数据版权归 [JingHao-Leon/geo-book](https://github.com/JingHao-Leon/geo-book) 所有；GEO Wiki 部分为 CC BY 4.0（卡内逐条标注"改编自 GEO Wiki"）；本仓库的蒸馏整理部分以 MIT 开源。版本历史见 [CHANGELOG.md](CHANGELOG.md)。
