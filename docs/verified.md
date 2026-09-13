# verified.md — 阶段 1.5 三重验证产出（geo-book-skill）

> 验证口径：task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）。
> 候选池：frameworks 27 + principles 84 = 111 条可执行候选；cases 37 / counter-examples 41 / glossary 30 按支持材料处理。
> 合并结果：12 个能力单元全部 verified；31 条候选被合并去重（见 rejected/）；20 条候选划为参考材料（见 references.md）；7 项缺口登记（见 needs-review.md）。
> 本阶段为纸面演练（walkthrough），实际输出评测在阶段 4 另测。

## 能力单元（12 个，全部 verified）

```yaml
- id: U1
  unit: geo-channel-map
  title: GEO 渠道决策树与六引擎信源地图
  type: procedure（决策树 + 画像体系）
  merged_candidates: [f15, f14, p41, p42, p43, p45, p46, p47, p48, p49, p50, p55, p56, p62, p63, p64, p06, p07, p26, p36]
  task_ids: [t01, t02]
  V1_source_sufficiency:
    passed: true
    reason: ch6/ch7 单处完整给出四步决策树、六引擎画像（引用率数字、头号信源、打法含义）、问题类型×渠道对照表；生态绑定定律有原文明示。口径冲突（p49 三口径）已按原文记录且不影响执行规则。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——"少儿英语机构（B 端课包 + C 端家长），预算有限，先做两个渠道"
    observed: 走决策树——①定引擎：家长决策人动线在微信（家长群/班级通知）与百度 → 必须覆盖元宝、文心（f20/p50/p63）；②看生态：元宝→公众号长文是入场券；文心→百家号+百科；③按题型修正：品牌对比题→中立对比表全网铺；"是不是智商税"信任题→挂投诉/政务数据+百家号；④形态：公众号长文版+百家号版。产出"引擎×渠道×形态"分工表。Kimi/豆包降档（豆包仅对比题有视频机会）。
  V3_task_utility:
    passed: true
    expected_benefit: 统一"发哪里"的决策口径，避免按平台名气或旧 SEO 经验铺渠道（知乎修正反例 x24 即此类错误）；数字快照需定期复核。
  decision: verified
```

```yaml
- id: U2
  unit: golden-question-formulas
  title: 三类黄金问题识别与内容公式（症状/对比/信任）
  type: framework + rule
  merged_candidates: [f16, p51, p52, p53, p54, p58, p66, p67]
  task_ids: [t03]
  V1_source_sufficiency:
    passed: true
    reason: ch8 单处完整：三大提问特征→三类黄金问题的识别特征、各内容公式、实测依据（六家趋同的"诊断决策树""分流式平衡答案""政法化引用"）。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——"聚水潭和旺店通哪个好"与"直播间没人看还要继续播吗"两道题
    observed: 前者=对比型（带候选名单要决断）→ 套分流公式：不自夸、按场景分流、给可核验标准（试用期/转人工率）、保留中立项，目标是进名单+分流理由有利；后者=症状型（描述病征）→ 套症状公式：症状做标题、排查决策树做骨架、分支给具体阈值（停播红线等）。识别-套用-产出均可复现。
  V3_task_utility:
    passed: true
    expected_benefit: 把"写什么形状的内容"从经验判断变成按动机分诊；给可检查的稿件骨架。
  decision: verified
```

```yaml
- id: U3
  unit: citable-content-spec
  title: 可引用内容四条硬指标（写作规范）
  type: checklist + rule
  merged_candidates: [p71, p72, p57, p65, p11]
  task_ids: [t04]
  V1_source_sufficiency:
    passed: true
    reason: ch10 单处完整给出四条硬指标（40-60 字结论前置 / 对比表 5+ 维度 / 价格带日期 / 数字可验证）及依据（被引与未引形态实测对比）；p57 补价格页三细则，p65 补"给结论、给数字、给适用边界"收束，p11 补质量三判据。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——一篇铺垫三段、无数据、价格为图片的产品稿
    observed: 按四指标逐条改写——开头 40-60 字给结论+适用边界；加 ≥5 维度对比表；价格改为文字页并标"2026 年 X 月官网价"；每个数字标注可查证来源。产出可机械核验的合格稿（改写前后对照四指标逐条打勾）。
  V3_task_utility:
    passed: true
    expected_benefit: 统一交稿验收口径（四项可机械检查）；直接针对"写了没被引"的形态性原因（x15/x36）。
  decision: verified
```

```yaml
- id: U4
  unit: geo-query-research
  title: GEO query 研究与分级（easy_win/target/skip）
  type: procedure + calculation
  merged_candidates: [f22, p68, p69, p70, p09, p10, p66]
  task_ids: [t06]
  V1_source_sufficiency:
    passed: true
    reason: ch10 第一步单处完整：捞词语料来源、三维分级口径（决策阶段×引用性×竞争度→easy_win/target/skip）、生产排序纪律（先 easy_win，10 条做透胜过 100 条平庸）；p09/p10 提供"优化问法""意图三分类/长尾"前置原则，p66 补价格锚点信号。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——跨境电商 ERP 行业，从百度下拉与知乎捞 10 条 query
    observed: 逐条标三维："聚水潭和旺店通哪个好"=选型×易引用×竞争空白→easy_win；"ERP 是什么意思"=纯定义→skip；"ERP 一年多少钱"=成本锚点→easy_win（引用潜力 high）。产出带分级的 query 清单表。缺字段时停止并标注而非猜值。
  V3_task_utility:
    passed: true
    expected_benefit: 统一分级口径（非 SEO 搜索量逻辑）；直接避免在纯定义类上白费产能（x34）。
  decision: verified
```

```yaml
- id: U5
  unit: one-fish-multi-platform
  title: 一鱼多吃多平台改造（三版 + 官网事实页）
  type: procedure
  merged_candidates: [f23, p73, p74, p33]
  task_ids: [t05]
  V1_source_sufficiency:
    passed: true
    reason: ch10 第三节单处完整：三版各自的对应引擎、字数/结构/挂源要求 + 官网事实页补充 + "改写而非复制粘贴"纪律（p74，低质 AIGC 识别特征）；p33 提供分出口思想源头。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——一份"客服机器人选型"研究底稿
    observed: 知乎问答版（真实问题标题+第一句结论前置+分场景对比表+负面占位）/ 公众号长文版（3000 字+开头摘要+文末挂权威源）/ 头条短文版（800-1500 字单点+一张对比表）/ 补官网事实页。三版口径一致、表达各异（复制粘贴检查不过）。
  V3_task_utility:
    passed: true
    expected_benefit: 一份研究覆盖多引擎供应链的改造成本最低路径；防"原样多平台铺发"降权（x37）。
  decision: verified
```

```yaml
- id: U6
  unit: geo-monitoring-iteration
  title: GEO 监测与迭代（三分支动作、两周周期、工具选型）
  type: procedure + decision
  merged_candidates: [f24, f25, p75, p76, p77, p37, p38, p36]
  task_ids: [t07]
  V1_source_sufficiency:
    passed: true
    reason: ch10 第四五六节单处完整：三分支迭代规则、两周周期、四类工具清单、买/建决策三条件、自建限速红线；p37/p38 提供度量口径（被引用率/描述倾向/对比站位）。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——某品牌 8 条 query 的监测结果（2 条被引、3 条竞品被引、3 条全无引用）
    observed: 分支一 2 条→固化形态复制到同 cluster；分支二 3 条→拆竞品被引稿（结论前置 or 数据更实）针对性改写；分支三 3 条→先查 query 类型（其中 1 条为纯定义类→接受低引用）再查渠道错配。两周后复查。工具路径：GEOBase 免费跑通（query<50 条→不自建）。
  V3_task_utility:
    passed: true
    expected_benefit: 监测结果→动作的确定性映射，避免"天天盯制造焦虑"（x40）或监测后无动作。
  decision: verified
```

```yaml
- id: U7
  unit: geo-test-protocol
  title: 引用行为实测规程（含先测后投与风控红线）
  type: procedure + troubleshooting
  merged_candidates: [f12, f13, f19, p03, p04, p05, p61, p78, p02]
  task_ids: [t15, t09, t14]
  V1_source_sufficiency:
    passed: true
    reason: ch6 实验设计单处完整（选题五动机/新对话纪律/逐字提问/口径几-12/n=1 方向性/多次采样），ch9 给先测后投流程（5 次独立采样→0 引用即红灯），ch6+ch10 给风控红线（约 30 次触发、分钟级间隔+每日上限）。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——"AI 填志愿靠谱吗"在元宝/豆包值不值得做内容
    observed: 设计 1 题 × 2 引擎 × 5 次独立新对话、逐字提问；记录每次是否带可提取引用（二值口径）；若 0/5 稳定零引用→亮红灯不投入或换引擎；有引用→看引用源级别是否够得着。全程人工间隔（分钟级）、当日总量受限。产出投入决策。
  V3_task_utility:
    passed: true
    expected_benefit: 防止在"引擎不联网的题"上白费产能（x31 元宝 0/5 警示）；防触发风控（x22）；统一数据口径防"9/12=75%"式误读（x21）。
  decision: verified
```

```yaml
- id: U8
  unit: negative-semantic-occupy
  title: 负面语义占位（抢阅卷权 + 烈度分级）
  type: procedure
  merged_candidates: [f18, p59, p60, p54, p48]
  task_ids: [t08]
  V1_source_sufficiency:
    passed: true
    reason: ch9 单处完整：负面句式为何是主战场、公关式否认无效的机理、分人群给结论的写法、老负面（阵地战）/新负面（先到先得）烈度分支、借第三方形态呈现（与 p54/p48 合读）。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——某学习机品牌面对"学习机是不是智商税"
    observed: 禁用"我们不是"式否认→写分人群判断框架（什么孩子值得买/什么情况是吃灰平板/价格构成账）→烈度判定：该题为存量老负面（知乎多题竞争）→打质量阵地战；差异点借第三方形态（资质、可验证案例、退费条款）。产出占位稿骨架。
  V3_task_utility:
    passed: true
    expected_benefit: 把品牌最怕的负面 query 从"回避"转为"定义权争夺"；给可检查的稿件结构（分人群+算账+识别标准）。
  decision: verified
```

```yaml
- id: U9
  unit: lso-local-playbook
  title: LSO 本地商户五步执行（诊断 + 执行清单）
  type: procedure
  merged_candidates: [f04, f05, p15, p16, p17, p18, p19, p20, p21, p22, p23]
  task_ids: [t11]
  V1_source_sufficiency:
    passed: true
    reason: ch2 单处完整：三要素诊断（相关性/距离/知名度）+ 三件套规则（NAP/评价运营/本地内容）+ 五步执行完整案例（少儿美术机构）。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——新开业的社区烘焙店
    observed: ①全平台搜店名认领并校准图钉→②定标准商户名统一 NAP、品类"烘焙"不贪大、简介带小区/学校名→③上架低门槛体验品+环境照→④交付满意时点邀请评价、差评认真回复转化→⑤每周带地名的门店内容。产出五步执行清单与检查点。
  V3_task_utility:
    passed: true
    expected_benefit: 门槛在执行完整度——清单防漏步；本地资产同时是 GEO 素材库（p23）。
  decision: verified
```

```yaml
- id: U10
  unit: vso-video-optimization
  title: VSO 视频搜索优化与双吃路径
  type: procedure
  merged_candidates: [f06, f07, p24, p25, p26, p27, p28, p29]
  task_ids: [t12]
  V1_source_sufficiency:
    passed: true
    reason: ch3 单处完整：双引擎模型、四件套（标题贴原句/关键词进字幕/合集/评论区置顶）、题型×形态分工（视频主攻对比题、图文兜底症状题）、双吃五步路径、语音三规则。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——选题"美缝发黄怎么办"（症状题）与"美缝剂品牌怎么选"（对比题）
    observed: 症状题：豆包 0/4 不联网警示→视频只做抖音搜索承接（标题贴原句+关键词进字幕+合集+置顶评论），另配图文/官方文档兜底 AI 引用；对比题：视频主攻（AI 几乎必引信源）。选词从评论区捞原话，开头 15 秒答案胶囊。产出双形态规划。
  V3_task_utility:
    passed: true
    expected_benefit: 防止"把宝全押视频做症状题"（x13）；一条内容喂两个搜索场景。
  decision: verified
```

```yaml
- id: U11
  unit: aeo-answer-optimization
  title: AEO 答案位三板斧与占位五步
  type: procedure
  merged_candidates: [f08, f09, p30, p31, p32, p33, p34, p35]
  task_ids: [t13]
  V1_source_sufficiency:
    passed: true
    reason: ch4 单处完整：三板斧技术细节（结构化问答/FAQPage schema/Speakable）、位置零价值边界（Ahrefs 12.3%/8.6%/19.6%）、AEO→GEO 承继三条推论、成本类五步占位例题。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——"ERP 实施要多久"成本/周期类问答页
    observed: ①标题用用户原话+更新日期→②第一段 40-60 字结论+免责锚点→③FAQPage JSON-LD 标子问题（每问配可独立摘引短答案）→④五维对比表（自建 vs 外包）→⑤公众号+百家号同口径分发。产出页面结构方案。
  V3_task_utility:
    passed: true
    expected_benefit: 把"被摘要/被引用"的形态要求工程化；FAQ 红利退潮时防止误拆结构化标记（p32/x16）。
  decision: verified
```

```yaml
- id: U12
  unit: brand-data-infrastructure
  title: 品牌数据基建三层（结构化数据/API 化/官方事实页）
  type: framework + checklist
  merged_candidates: [f26, f27, p81, p82, p83, p13]
  task_ids: [t10]
  V1_source_sufficiency:
    passed: true
    reason: ch11 单处给出三层模型与三类读者行动清单；第三层（官方事实页）有实测支撑（Kimi 67.6% 官网覆盖率、晓多博客进三家引用）；第一、二层为推演（章内已标注），不冒充实测。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: 新输入——某 SaaS 品牌要"本周就把自家院子扫干净"
    observed: 本周：盘点官网事实页（产品参数/价格带日期/对比维度/常见质疑官方回应）→三个月：核心信息 Schema 结构化、全渠道口径对齐→持续：监测出现率与口径、负面词条占位。产出带时间窗的基建清单（层 2 API 化标注"推演、按需"）。
  V3_task_utility:
    passed: true
    expected_benefit: 把"长期底座"拆成有节奏的动作；防止只有内容打法没有事实底座（x41 官方口径缺位被别人填）。
  decision: verified
  notes: 层 1/2 的 Agent 时代收益属推演，进 B 段与 needs-review；执行动作本身（建事实页、上结构化标记）不依赖推演成立。
```

## 参考材料（20 条 → references.md）

f01, f02, f03, f10, f11, p01, p02, p08, p12, p13, p14, p23(并 U9), p31(并 U11), p36(并 U1/U6), p39, p55(并 U1), p56(并 U1), p80, p84, 以及 glossary 30 条、cases 37 条、counter-examples 41 条的支持材料映射详见 references.md 与 coverage-audit.md。

## 判定汇总

| 判定 | 数量 | 说明 |
|---|---|---|
| verified | 12 单元（合并 111 条可执行候选） | 全部 V1/V2/V3 通过 |
| reference | 10 条原则/框架候选 + 术语 30 + 案例 37 + 反例 41 | 映射到 overview/glossary/卡片 R-A-B 段 |
| needs_review | 7 项缺口 | 见 needs-review.md，均已转化为 B 段约束或使用说明，不阻断交付 |
| rejected | 20 条合并去重记录 | 见 rejected/，均为候选池双份记录，无"无原文依据"被淘汰项 |
