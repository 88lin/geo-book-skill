# geo-book-skill

> 从《[从 SEO 到 GEO：AI 时代的搜索优化实战手册](https://github.com/JingHao-Leon/geo-book)》（JingHao-Leon 著，MIT License）蒸馏出的**可执行 Agent Skill 包**——把书里的 GEO（生成式引擎优化）方法论拆成 12 张原子能力卡，让 AI 助手在你的真实工作里直接用起来。

蒸馏基于 [cangjie-skill](https://github.com/) 的 RIA-TV++ 流水线（整书理解 → 五路并行提取 → 三重验证 → 晋级门 → RIA 能力卡 → 压力测试 → 编译交付），全部审计轨迹见 [`docs/`](docs/)。

## 这是什么

一个可直接安装的 Skill（`geo-playbook/`）：当你在 AI 助手（Claude Code / ZCode 等）里问出下面这类问题时，它会被自动触发并按书中的实测方法给出结构化回答：

- "我们是做 CRM 的，内容应该先发到哪些平台？要不要做知乎？"
- "豆包和元宝引用内容的偏好有什么区别？"
- "'群晖和威联通哪个好'这篇文章该怎么写？"
- "为什么我的对比文章 AI 从来不引用？"
- "想把这篇研究一稿多发到公众号、知乎、头条，怎么改？"
- "GEO 内容发了两个月，怎么知道有没有效果？"
- "品牌被问'是不是智商税'，怎么应对？"

## 13 张能力卡

| 能力卡 | 一句话 | 出处 |
|---|---|---|
| geo-channel-map | 先按用户动线定主攻引擎，再按生态绑定与题型定渠道形态（含六引擎信源画像） | 第 6/7/9 章 |
| golden-question-formulas | 按提问动机分诊症状/对比/信任三类黄金问题，各套内容公式 | 第 8 章 |
| citable-content-spec | 可引用内容四条硬指标：结论前置 40-60 字、对比表 5+ 维度、价格带日期、数字可验证 | 第 10 章 |
| geo-query-research | 从真实语料捞 query，按决策阶段×引用性×竞争度分级，先做 easy_win | 第 10 章 |
| one-fish-multi-platform | 一鱼多吃：知乎问答版/公众号长文版/头条短文版+官网事实页，改写而非复制 | 第 10 章 |
| geo-monitoring-iteration | 两周周期监测被引用率/描述倾向/对比站位，按三分支迭代 | 第 10 章 |
| geo-test-protocol | 引用行为实测规程：独立新对话、逐字提问、二值口径、先测后投、限速红线 | 第 6/9 章 |
| negative-semantic-occupy | 负面语义占位：抢阅卷权，分人群给结论，借第三方形态呈现 | 第 9 章 |
| lso-local-playbook | 本地商户五步执行（NAP/评价运营/本地内容） | 第 2 章 |
| vso-video-optimization | 视频搜索四件套与"AI 引视频"双吃路径 | 第 3 章 |
| aeo-answer-optimization | AEO 三板斧与答案位占位五步 | 第 4 章 |
| brand-data-infrastructure | 品牌数据基建三层（官方事实页有实测支撑，API 化属原书推演） | 第 11 章 |
| ai-crawler-access | AI 爬虫按用途三类决策（训练/检索/用户触发，屏蔽检索类=立即失去被引）+ llms.txt 低成本预部署 | **补充自 GEO Wiki**（CC BY 4.0） |

## 安装

**ZCode / Claude Code（用户级，所有项目可用）：**

```bash
git clone https://github.com/88lin/geo-book-skill.git
mkdir -p ~/.zcode/skills   # Claude Code 用 ~/.claude/skills
cp -r geo-book-skill/geo-playbook ~/.zcode/skills/
```

重开会话即可。也可以只复制 `SKILL.md` + `references/` 到任意项目的 `.claude/skills/` 或 `.zcode/skills/`。

**重新编译（可选）：** `bundle/` 是唯一事实源（Capability Bundle），可用 cangjie-skill 的编译器改出 pack 模式（1 个路由入口 + 7 个独立 Skill）：

```bash
python3 scripts/cangjie.py compile --bundle <path>/bundle --out dist/geo-book-skill --output pack --yes
```

## 数据边界（重要）

- 全部引擎信源数字来自 **2026-08-05 单日、单账号**实测（12 题 × 6 引擎 + 97 次多次采样），原书自认打法保质期约两三年——Skill 内置了"方向性使用、定期复核、先测引用再投入"的纪律，但请勿把任何数字当统计铁律引用。
- 实测覆盖广告电商与教育两行业，其他行业的"决策人-引擎"映射是外推。
- 原书未提供"被引用 → 商业结果"的 ROI 数据；本 Skill 不承诺转化效果。
- v0.2.0 起合入 [GEO Wiki](https://geo.wiki/zh)（CC BY 4.0）的部分内容（AI 爬虫/llms.txt/可引用性七信号/GEO 指标口径），改动均在能力卡内逐条标注"改编自 GEO Wiki"；爬虫名单变化快，llms.txt 的引擎读取截至 2026-05 未获厂商确认。
- 红线（Skill 会主动拒绝）：刷评刷量、编造数据、伪装中立洗地、高频自动化抓取（约 30 次连续提问触发 DeepSeek 风控）。

## 目录结构

```
geo-playbook/          # 安装这个：编译产物（1 入口 + 12 能力卡 + 速查/术语/概览）
bundle/                # Capability Bundle（verified.yaml + 12 张 RIA 卡），可重新编译
docs/                  # 蒸馏审计轨迹
  DIGEST.md            #   面向读者的精华长文（约 8000 字）
  BOOK_OVERVIEW.md     #   阶段 0：整书理解（骨架/术语/批判/15 项关键任务）
  verified.md          #   阶段 1.5：三重验证记录
  coverage-audit.md    #   任务级覆盖审计
  test-results.md      #   阶段 4：触发盲测 31/31 + 输出评测 24/24
  candidates/          #   阶段 1：219 条原始候选
  rejected/            #   去重记录
  …
```

## 测试

首版：触发盲测（独立 agent、含跨 Skill 诱饵）**31/31**、路由可达 5/5、输出评测（12 能力 × 正常+边界）**24/24**。v0.2.0 回归：触发盲测 **15/15**（含新卡路由 4/4 与"爬虫代码"无关诱饵防误触发）、输出评测 **6/6**（新卡拒绝"AI 爬虫全部 Disallow"反模式），边界场景全部正确"先询问/停下/拒绝"。详见 [`docs/test-results.md`](docs/test-results.md)。

## License

MIT（继承原书许可）。原书与实测数据版权归 [JingHao-Leon/geo-book](https://github.com/JingHao-Leon/geo-book) 所有，本仓库的蒸馏整理部分同样以 MIT 开源。
