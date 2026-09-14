# Changelog

本仓库遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 精神，版本号语义：次版本号 = 能力卡内容或来源的实质变更。

## [0.4.2] - 2026-09-15

### Added
- 七卡穷尽审查补充块（三源 ~177 候选项中高价值项合入）：
  - ai-crawler-access：Bytespider 实测不遵守 robots.txt、26 令牌全名单、Extended 令牌不是真实 UA、RFC 9309 语义纠错、llms.txt 工程细则与纠错（llms-full.txt 不在原始规范、Google 已书面表示不使用）
  - brand-data-infrastructure：结构化数据四级台阶审计法、生成五规则、十分项评分表、废弃/受限类型更新、品牌权威综合分两套口径
  - citable-content-spec：段落可引用量化判据、对题性 r=0.432 最强预测因子、五类抽取块权重与实测增益、FAQ 纠错（纯 Q&A 格式 −5.7%）、E-E-A-T 代理信号与伪造四反模式、平台结构偏好差异
  - geo-channel-map：引用位置第二把尺子、信源四层优先级框架、引擎三分类法、海外对照数字
  - geo-monitoring-iteration：Position 三种不兼容定义、Citation Rate 区间、L1–L5 成熟度阶梯、报告七陷阱、修复优先级判据、变更风险分级、周检轻量节奏、AI 流量领先指标
  - geo-test-protocol：问题类型触发检索、国产平台 API 采样坑（千问/火山方舟/元宝）、API 度量字段、方法论免责五条
- GLOSSARY 追加 s17–s25（可信最重要、SEO/GEO 60/40、答案引擎术语纠错、llms.txt 纠错组、Bytespider 不遵守 robots、新兴声明标准、4-8 周见效、可抽取事实块、geo-citation-lab）

### Verified
- 13 卡六段结构（R/I/A1/A2/E/B + 相关能力）完整
- 部署产物与源码一致，三份 glossary 副本同步

## [0.4.1] - 2026-09-14

### Added
- 三源补遗核对后的补入：
  - brand-data-infrastructure / aeo-answer-optimization：标记≠引用、sameAs 最高优先级、类型优先级、两类解析器对错误标记的相反处理（GEO Wiki schema-org-for-ai，searchVIU 2025）
  - geo-test-protocol：采样证据等级 A–D（个人账号自动降 D）、采样环境四档不混算、"没提到也要记录"
  - geo-monitoring-iteration：指标至少四层（提及率/首位率/描述准确率/引用质量）+ 海外"广度≠深度"（Perplexity 均引 16.35 源 vs ChatGPT 6.88 但单条影响力 5.64 倍）
  - citable-content-spec：E-E-A-T 四维 0-25 量化口径
  - brand-data-infrastructure：事实卡实践（来源/核验日期/证据等级 A–E，查不到标待确认）

### Verified
- 全量完整性复查：13 卡六段结构完整、安装产物与源一致（仅编译器资源清单为预期差异）、三参考仓库有价值项逐一对照

## [0.4.0] - 2026-09-14

### Added
- 合入 geo-seo-claude（zubair-trabzada，MIT）的方法与资产：
  - citable-content-spec：段落级量化评分细则（答案块 30/自包含 25/结构 20/统计密度 15/独特性 10；段落 134–167 词最优）
  - geo-monitoring-iteration：GEO Score 六维加权公式 + 品牌权威平台分值表（Ahrefs 2025-12：YouTube 相关性 0.737 最强、外链 0.266 弱）
  - brand-data-infrastructure：6 个可直接填写的 JSON-LD 模板（随 resources 分发：organization/software-saas/product-ecommerce/local-business/article-author/website-searchaction）
- README 新增 geo-seo-claude 配套条目；LICENSE 增补模板作者版权行
- 仓库标准化：AGENTS.md（Codex/Cursor 入口）、prompts/ 纯提示词版、三篇使用教程、README 全面重写、CHANGELOG 建立

### Changed
- README 不再列蒸馏工具链条目（审计轨迹保留于 docs/）

## [0.3.0] - 2026-09-14

### Added
- 合入 GeoLook（aigclink/geolook，MIT）CN-GEO 数据集 v2.0.1（187,818 条去重引用实算）的大样本结论，并入 5 张能力卡：
  - geo-channel-map：官网 1.37% 定律、榜单站 9.1%、各引擎生态集中度（百度 AI/文心 66%+、DeepSeek 21.8% 最中立、千问吃夸克 19.2%）、Web≠App 口径
  - geo-test-protocol：Web ≠ App 采样口径纪律（千问两端信源重合仅 24.5%）
  - ai-crawler-access：四层依赖模型（访问→定向→理解→可引用，框架来自 GeoReady）+ SPA 空壳 / WAF-UA 探测 / X-Robots-Tag 检查点
  - geo-monitoring-iteration：归因三段链路（采样 → referrer/UTM → 转化事件）
  - brand-data-infrastructure：官网"事实源而非引用源"定位校正
- GLOSSARY 增补 s09–s12（GeoLook 口径）；book/overview 增补配套关系
- 回归：输出评测 2/2，validate_skill_pack 0 errors

## [0.2.0] - 2026-09-14

### Added
- 新增第 13 张能力卡 `ai-crawler-access`（AI 爬虫三类放行策略 + llms.txt），改编自 GEO Wiki（CC BY 4.0）
- citable-content-spec 并入可引用性七个结构信号；geo-monitoring-iteration 并入"引用≠提及≠链接"与 GEO 十项 KPI 口径
- GLOSSARY 增补 8 条补充词条（s01–s08）；book/overview 增补答案循环 / LLMO / 零点击机制层

### Fixed
- also_read 使用完整 capability_id 导致编译 broken-ref，改为 slug 后通过

### Tested
- 触发盲测 15/15（含新卡路由与无关诱饵防误触发）；输出评测 6/6（含拒绝"AI 爬虫全部 Disallow"反模式）

## [0.1.0] - 2026-09-13

### Added
- 首次发布：从《从 SEO 到 GEO：AI 时代的搜索优化实战手册》（JingHao-Leon，MIT）蒸馏
- 12 张 RIA 能力卡（7 晋级 + 5 路由），single 模式编译产物 `geo-playbook/`
- 全流水线审计轨迹（219 条候选 → 三重验证 → 晋级门 → 压力测试）

### Tested
- 触发盲测 31/31、路由可达 5/5、输出评测 24/24（12 能力 × 正常+边界）
