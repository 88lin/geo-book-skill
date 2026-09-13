# Changelog

本仓库遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 精神，版本号语义：次版本号 = 能力卡内容或来源的实质变更。

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
