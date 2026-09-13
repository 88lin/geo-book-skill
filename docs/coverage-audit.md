# coverage-audit.md — 原书关键任务 → 候选 → 判定 → 交付去向（geo-book-skill）

> 基准：BOOK_OVERVIEW.md 的 15 项关键任务清单（不从旧 verified 反推）。
> 判定来源：verified.md（阶段 1.5）；去向含阶段 1.6 晋级结果（promoted / router）。

| task_id | 读者任务 | 原文位置 | 候选 | 判定 | 实际交付去向 |
|---|---|---|---|---|---|
| t01 | 判断目标用户在哪个 AI 引擎提问，定主攻引擎 | ch7 决策树第一步；ch9 家长决策链 | f14, f20, p50, p63 | verified（并入 U1） | 能力卡 geo-channel-map（promoted） |
| t02 | 为引擎 × 问题类型选内容分发渠道与形态 | ch7 决策树 + 题型表 | f15, p41~p49, p55, p56, p62, p06, p07, p26, p36 | verified（并入 U1） | 能力卡 geo-channel-map（promoted） |
| t03 | 判断 query 属哪类黄金问题并套内容公式 | ch8 三大特征 | f16, f17, p51~p54, p58, p66, p67 | verified（并入 U2） | 能力卡 golden-question-formulas（promoted） |
| t04 | 生产"可被引用"的内容 | ch10 四条硬指标 | p71, p72, p57, p65, p11 | verified（并入 U3） | 能力卡 citable-content-spec（promoted） |
| t05 | 一份内容改造多平台形态 | ch10 一鱼多吃 | f23, p73, p74, p33 | verified（并入 U5） | 能力卡 one-fish-multi-platform（promoted） |
| t06 | 建 query 清单并分级排序 | ch10 第一步 | f22, p68, p69, p70, p09, p10, p66 | verified（并入 U4） | 能力卡 geo-query-research（promoted） |
| t07 | 搭建监测并按结果迭代 | ch10 四五六节；ch6 风控 | f24, f25, p75, p76, p77, p37, p38；风控 p78/f13 归 U7 | verified（并入 U6；风控并入 U7） | 能力卡 geo-monitoring-iteration（promoted）+ geo-test-protocol（promoted） |
| t08 | 负面语义 query 占位 | ch9 负面语义占位 | f18, p59, p60, p54, p48 | verified（并入 U8） | 能力卡 negative-semantic-occupy（router） |
| t09 | 先测引用再决定投入 | ch9 AI 原生场景 | f19, p61 | verified（并入 U7） | 能力卡 geo-test-protocol（promoted） |
| t10 | 品牌数据基建三层 | ch11（推演章） | f26, f27, p81, p82, p83, p13 | verified（并入 U12；层 1/2 推演进 B） | 能力卡 brand-data-infrastructure（router） |
| t11 | 本地门店 LSO 完整执行 | ch2 | f04, f05, p15~p23 | verified（并入 U9） | 能力卡 lso-local-playbook（router） |
| t12 | 视频内容搜索/GEO 双吃优化 | ch3 | f06, f07, p24~p29 | verified（并入 U10） | 能力卡 vso-video-optimization（router） |
| t13 | 网页内容 AEO 答案位优化 | ch4 | f08, f09, p30~p35 | verified（并入 U11） | 能力卡 aeo-answer-optimization（router） |
| t14 | 合规边界（风控/灰产/伦理） | ch5.5；ch10 第五节 | p78, f13, p40, p74, p79, p39, p84 | verified（红线并入 U7 执行；其余进相关卡 B 段与入口原则） | geo-test-protocol B 段 + citable/one-fish B 段 + entry core_principles |
| t15 | 用正确口径做引用行为实测 | ch6 实验设计 | f12, p03, p04, p05 | verified（并入 U7） | 能力卡 geo-test-protocol（promoted） |

## 无对应可执行任务的内容（有意不做成能力）

| 内容 | 原文位置 | 去向 | 理由 |
|---|---|---|---|
| 五代演进分层模型 f01 | 前言/ch11 | book/overview.md 参考区 | 宏观坐标模型，供理解与 B 段引用 |
| 角色阅读地图 f02 | 前言 | book/overview.md 参考区 + DIGEST | 阅读路线，非领域方法 |
| 图书馆流水线 f03 | ch1 | book/overview.md 参考区 | SEO 机制底座素材 |
| 导购员总比喻 f10 | ch5 | book/overview.md + 各卡 R/I 段 | 核心比喻，R/A 素材 |
| SEO→GEO 三层区别 f11 | ch5 | book/overview.md + monitoring 卡 B 段 | 坐标转换解释框架 |
| 动机层数据 p01/p39/p80/p84 | 前言/ch5/ch11 | book/overview.md + DIGEST | "为什么做"的论据与推演，非操作规则 |
| SEO 家族背景 p08/p12/p13/p14 | ch1 | book/overview.md 参考区 | 通用知识章，作者亦标注"通用知识为主" |
| 全部案例 c01~c37 | 各章 | 各能力卡 A1 段 + DIGEST | 支持材料 |
| 全部反例 x01~x41 | 各章 | 各能力卡 B 段 + DIGEST 陷阱节 | 支持材料 |
| 全部术语 g01~g30 | 前言等 | GLOSSARY.md → book/glossary.md | 词典 |

## 覆盖结论

- 15/15 项关键任务均有候选、判定与去向；无未解释遗漏。
- 高重要性任务（t01/t02/t03/t04/t05/t06/t07/t14/t15）全部落在 promoted 能力或入口原则层。
- 待核查项（见 needs-review.md）均为数据时效/口径/推演类缺口，已转化为卡片 B 段约束，不影响方法可执行性。
