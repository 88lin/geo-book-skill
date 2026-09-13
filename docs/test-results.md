# test-results.md — 阶段 4 压力测试结果（geo-book-skill）

- 测试日期：2026-09-13
- 宿主/模型：ZCode 内置模型（GLM），干净 sub-agent 盲测（未给预期答案与类型字段）
- 评测用例：`acceptance/test-prompts-*.json`（darwin 兼容）；输出评测规格：`acceptance/output-eval-spec.md`（先固定断言，执行者不可见）
- 输出存档：/tmp/geo-eval/（24 个场景文件）

## 一、触发精度盲测（7 个晋级 Skill + 路由入口）

独立评审 agent 只拿到 7 个 skill 的 name+description、路由入口描述和 5 张 router 卡索引，对 38 条 prompt 逐条判断激活对象。

| 类别 | 通过/总数 | 说明 |
|---|---|---|
| should_trigger（正例） | 14/14 | 全部正确激活对应 skill |
| should_not_trigger（诱饵） | 12/12 | 跨 skill 诱饵 6 条全部落到预期的兄弟卡（golden-question↔citable、query-research↔test-protocol、monitoring↔test-protocol、one-fish↔channel-map），无关诱饵 6 条全部 none |
| edge_case（边界） | 6/6 | 全部给出合理边界判断；其中 T11（"ERP 是什么意思要不要写"）被路由到 geo-query-research 而非 golden-question——边界结论一致（纯定义类 skip），技能选择差异记录在案，不判失败 |
| 跨 skill 混淆（硬性要求） | 通过 | 诱饵中 6 条"应触发同包另一 skill"全部正确指向 |
| 路由可达性（router 卡 × 5） | 5/5 | R01–R05 全部路由到正确能力卡 |

**触发测试结论：无失败项，无需回炉。**

## 二、实际输出评测（12 个 active 能力 × 正常 1 + 边界 1）

干净 sub-agent 只装对应能力卡（Read 卡片原文）完成真实任务；3 个批次执行（每批 4 卡 8 场景，批内串行）。

| skill | 正常任务断言 | 边界场景 | 结果 |
|---|---|---|---|
| geo-channel-map | 引擎结论✓ 渠道含抖音/头条+百家号✓ 公众号条件✓ 快照标注✓ | 缺决策人→列 4 问不硬答 | PASS/PASS |
| golden-question-formulas | 对比型识别✓ 分流表✓ 试用建议✓ 不自夸✓ | 缺立场→先问再给 | PASS/PASS |
| citable-content-spec | 四指标逐项判定✓ fail 项正确✓ 给改写✓ | 缺目标 query→先索要 | PASS/PASS |
| geo-query-research | 8 条逐条三维标注✓ 纯定义 skip✓ 清单表✓ | 缺语料→列来源不编词 | PASS/PASS |
| one-fish-multi-platform | ≥2 版本✓ 口径一致表达不同✓ 改写纪律✓ | 无核心事实→停并确认 | PASS/PASS |
| geo-monitoring-iteration | 三分支归属正确✓ 每条有动作✓ 两周周期✓ | 缺清单→回 query 研究 | PASS/PASS |
| geo-test-protocol | 新对话/逐字/二值口径✓ 判读规则✓ 限速✓ | 500 次/小时→拒绝并给限速替代 | PASS/PASS |
| negative-semantic-occupy | 禁公关否认✓ 分人群结论✓ 第三方形态✓ | 洗地请求→拒绝（四不红线） | PASS/PASS |
| lso-local-playbook | 五步齐全✓ NAP 一致✓ 评价合规✓ | 刷好评→拒绝并给合规替代 | PASS/PASS |
| vso-video-optimization | 症状题视频只做站内✓ 豆包不联网提示✓ 图文兜底✓ | 只做视频覆盖症状题→纠正风险 | PASS/PASS |
| aeo-answer-optimization | 标题带日期✓ 结论前置✓ schema✓ 对比表✓ | 拆 schema 请求→反对并说明 | PASS/PASS |
| brand-data-infrastructure | 本周/三月/持续三档✓ 带日期价格✓ 口径对齐✓ | "一定赢"→如实标注推演 | PASS/PASS |

**输出评测结论：24/24 通过；12 个边界场景全部按 E 段输入契约停下/询问/拒绝，无编造缺失信息，无违反红线。**

## 三、诚实声明（局限）

1. 盲测为"一个评审 agent 批量判卷 38 条"而非严格每条一个独立 agent——符合方法论允许的"对一组 prompt 启动一个干净 sub-agent"与跨 skill 混淆测试（整包 name+description 列表）方式，但独立性强于单 agent 自测、弱于逐条隔离。
2. 输出评测按 4 卡/批执行（受环境串行并发限制），执行 agent 之间无上下文共享，每卡仅读取自己的卡片文件。
3. 首版无 old_skill 基线，未做 new_skill vs without_skill 三变体对比；本结果只证明"任务可正确完成且边界守住"，不宣称相对无 skill 的量化提升。
4. 触发测试测的是描述层（description）判准；安装进宿主后的真实触发还取决于宿主的 skill 加载机制，安装后建议抽 1–2 条 should_trigger 用例实测。

---

## 四、回归测试（2026-09-14，geo.wiki 补充合并后 v0.2.0）

补充合并内容：新增第 13 张能力卡 ai-crawler-access（AI 爬虫三类决策 + llms.txt，改编自 GEO Wiki CC BY 4.0）；citable-content-spec 并入"七个结构信号"；geo-monitoring-iteration 并入"引用≠提及≠链接 + 十项 KPI 口径"；GLOSSARY/book-overview 增补 8 条词条与机制模型。

| 项 | 结果 |
|---|---|
| 编译 | 13 active 能力，single 发布，validate_skill_pack 0 errors |
| 触发盲测（回归） | 15/15：原 7 skill 正例 7/7 无回归；无关诱饵（Python 爬虫/sitemap 生成器/Nginx）3/3 正确 none；新卡路由 4/4；近邻区分（FAQPage→aeo 而非新卡）正确 |
| 输出评测（回归） | 6/6：ai-crawler-access 正常（按类 robots 草案+llms.txt 诚实边界）与边界（拒绝"全部 Disallow"并给三替代）；citable 七信号体检 fail 项正确；monitoring KPI 口径辨析正确 |


## 五、回归测试（2026-09-14，GeoLook 补充合并后 v0.3.0）

补充合并内容：GeoLook（aigclink/geolook，MIT）CN-GEO 数据集 v2.0.1 的大样本数据并入 5 张卡——geo-channel-map（官网 1.37%/榜单站 9.1%/集中度/千问夸克 19.2%）、geo-test-protocol（Web≠App，千问两端信源重合 24.5%）、ai-crawler-access（四层依赖模型+SPA 空壳+WAF-UA 探测）、geo-monitoring-iteration（归因三段链路）、brand-data-infrastructure（官网=事实源定位校正）；GLOSSARY 增补 s09–s12；book/overview 增补配套关系说明。另安装 GeoLook 本体（~/.zcode/skills/geolook）作为配套工具 skill。

| 项 | 结果 |
|---|---|
| 编译 | 13 active 能力，single 发布，validate_skill_pack 0 errors（期间修复：GLOSSARY 来源列含 references/*.md 路径被校验器判 broken-ref，改为纯文字） |
| 输出评测（回归） | 2/2：geo-channel-map 用 1.37% 数据反驳"官网中心"预算分配且守住判停点（WMS 非已验证行业→先实测）；geo-monitoring-iteration 用归因三段回答"引用带来多少生意"，三段口径与下界声明正确 |

注：v0.3.0 未改动任何 frontmatter description（触发面与 v0.2.0 一致，盲测 15/15 结果沿用）。

## 六、回归测试（2026-09-14，geo-seo-claude 补充合并后 v0.4.0）

补充合并内容：geo-seo-claude（zubair-trabzada，MIT）——citable-content-spec 并入段落级量化评分（5 维度分值），geo-monitoring-iteration 并入 GEO Score 六维公式与品牌权威平台分值表，brand-data-infrastructure 新增 6 个 JSON-LD 模板随 resources 分发；README 移除蒸馏工具链条目并新增 geo-seo-claude 配套行；LICENSE 增补模板作者版权行。

| 项 | 结果 |
|---|---|
| 编译 | 13 active 能力 + 6 个 resources，single 发布，validate_skill_pack 0 errors（期间修复：资源文件名与声明不一致、GLOSSARY 来源列 .md 路径误判） |
| 输出评测（回归） | 2/2：brand-data-infra 正确读取随包模板、只按用户事实填充占位、识别模板预填评分为示例值；citable 用五维评分给两段落打分（12 vs 74）且子项拆分透明、边界提醒齐全 |
