# Changelog

本仓库遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 精神，版本号语义：次版本号 = 能力卡内容或来源的实质变更。

**1.0.0 是定稿版**——内容、结构与校验流程均已稳定，作者不再计划后续迭代。数据本身仍会随引擎行为漂移，使用时按各卡的「方向性 + 定期复核」纪律处理（见 [数据边界](README.md#-数据边界与红线请务必读)）。

## [1.0.0] - 2026-09-18

### Added
- `geo-playbook/references/workflow.md`：全流程执行编排（原书五步 + 两道闸门）——第 −1 步适用性确认（国内/海外、是否本地门店、有无内容资产）+ 0→6 步依赖顺序（可访问性 → query 分级 → 渠道分工 → 先测后投闸门 → 内容生产 → 分发 → 监测迭代），每步给入口卡、该问什么、产出模板、参考工期与判停点，另附七条快捷路径
- `geo-playbook/resources/` 从 6 个扩到 19 个模板：
  - 补齐卡内点名却未分发的 `schema-faqpage.json` / `schema-howto.json` / `schema-breadcrumb.json`
  - `robots-ai-crawlers.txt`（按训练/检索/用户触发三类放行，含 26 令牌全名单、RFC 9309 specificity 陷阱、部署后必验三件事）
  - `llms.txt.template`（硬格式、收录三档、误用清单、三条诚实边界）
  - `resources/templates/` 七张产出物表格：渠道分工表、query 分级表、稿件体检表、分发对照表、实测记录表、双周迭代表、NAP 对照表——对应各卡 E 段承诺的输出格式
  - `resources/README.md` 模板索引
- `scripts/validate.py` 一致性校验 + `.github/workflows/validate.yml` CI：六段结构、四方一致（SKILL.md 路由表 ↔ capability-index ↔ cheatsheet ↔ verified.yaml ↔ 磁盘）、相对链接、技能内反引号裸路径可从所在文件打开、JSON-LD 可解析、编号式补充块检测
- `scripts/gen_schema_templates.py`：九份 JSON-LD 模板的统一生成器
- cheatsheet 新增四节：关键数字速查（带口径）、红线与拒绝项、判停点速查、口径纪律

### Changed
- SKILL.md：`description` 从内容目录式改为「何时使用 / 何时不使用」触发导向；新增「回答纪律」七条与随包资源索引；路由表去掉重复路径前缀
- JSON-LD 模板本地化为国内口径：`addressCountry: CN`、`+86` 电话、`CNY`、`zh-CN`、七天无理由退货、`KGM` 计重，`sameAs` 改为知乎/微博/百度百科/企查查/B站/小红书/高德/百度地图/点评/美团（原为 Yelp/BBB/Facebook/Crunchbase/LinkedIn）
- 能力卡补充块统一为「**补充 · 标题**（来源）」，替换原先断裂的编号体系
- 9 张能力卡新增「配套资源」段，指向对应模板
- `bundle/verified.yaml`：`card` / `resources` 路径重指向 `geo-playbook/`，并为 9 个能力补齐资源清单
- AGENTS.md / prompts 纯提示词版同步 workflow 顺序、模板索引与口径纪律

### Fixed
- `bundle/` 与 `geo-playbook/` 逐字节重复的 20 个文件（约 180KB）——删除重复副本，`geo-playbook/` 成为唯一事实源，`bundle/` 只保留 verified.yaml 登记表。重复副本中 `bundle/cards/brand-data-infrastructure.md` 的 6 条 resources 链接因目录深度不同全部失效，随之修复
- `docs/DIGEST.md` 的 17 条链接指向不存在的编译产物路径 `dist/geo-book-skill/`，改为 `../geo-playbook/`
- `docs/GLOSSARY.md` 与 `geo-playbook/references/glossary.md` 重复，删除前者
- `docs/PIPELINE_STATE.md` 泄漏的构建机绝对路径与过期的阶段标记
- README 测试徽章与测试表缺 v0.4.0 / v0.4.2 / v0.5.0 轮次

**以下为同版内回归评测发现并修复：**

- **20 条路径引用打不开**：新文件混用"文件相对"与"技能根相对"两种基准，其中 14 条从任何基准都解析不了。全部改为可校验的相对链接；`validate.py` 增加"裸路径引用从所在文件可打开"检查防复发
- **workflow 缺国内/海外适用性分流**："跨境电商""出海 SaaS"这类词会直接误入国内引擎流程。新增第 −1 步适用性确认（国内/海外、是否本地门店、有无内容资产）
- **workflow 第 0/3/4/5/6 步缺"输入 / 缺什么先问"**：只有第 1/2 步有，agent 走到第 0 步会直接给 robots 建议而不先索取现状。五步补齐
- **稿件体检表误判平台短文**：结构硬指标（段落 ≥25、H2 ≥6、字数地板 1500）来自海外长文研究，会把符合 one-fish 规范的 800–1500 字头条短文判成全 fail。新增适用范围表按稿件类型分档
- **schema 模板预填像真数据的评分**：`ratingValue: 4.8 / 4.6` 与 `XX` 式占位符风格不一致，忘改即等于发布伪造评分，同时踩"不伪造评价"红线与"数字可验证"硬指标。改为 `X.X` 这类填不满的形式，三处补专项警告
- workflow 缺工期锚点（补每步参考工期 + 排期口径声明）、第 5 步缺产出物模板（新增 `distribution-matrix.md`）、体检表两套百分制并列无说明、文件名"五步工作流"与实际七段不符、robots 模板 Crawl-delay 作用面易误读、brand-data 卡"9 个模板"只列 6 个名

### Verified
- `python scripts/validate.py` 0 errors 0 warnings；负向测试确认可捕获断链、缺段、编号式补充块、裸路径失效
- v1.0.0 回归评测四场景全部 PASS：E1 从零跑完整项目 30→38/40、E2 跳过闸门边界 37/40、E3 稿件体检 31→38/40、E4 robots+llms.txt+schema 38→39/40。报告见 `docs/supplement-audits/v1.0.0-workflow-templates-audit.md`（含"自评非独立盲测"的局限声明）

## [0.5.0] - 2026-09-15

### Verified
- v0.4.2 回归评测通过（两场景均 38/40 PASS）：
  - ai-crawler-access：robots.txt + llms.txt 审查场景，补充块利用率 10/10
  - geo-monitoring-iteration：从零搭建监测体系场景，补充块利用率 10/10
- 审计报告存档于 `docs/supplement-audits/`

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
