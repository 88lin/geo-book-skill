# AI 爬虫可访问性与 llms.txt

> 能力单元 ai-crawler-access ｜ 来源：**补充来源，超出原书范围**——改编自 GEO Wiki（CC BY 4.0）：https://geo.wiki/zh/ai-crawlers 、https://geo.wiki/zh/llms-txt （2026-09 核对）。原书《从 SEO 到 GEO》未覆盖本条目。

## R — 原文

> "屏蔽训练类不会影响检索类；屏蔽检索类会让内容立即不再出现在 AI 答案中。"（GEO Wiki《AI 爬虫》）
>
> "llms.txt 是一项尚处于提案阶段的发布约定……它让页面更易读取，既不控制访问，也不帮助引擎发现内容。"（GEO Wiki《llms.txt》）

出处：GEO Wiki《AI 爬虫》《llms.txt》（CC BY 4.0，改编）。

## I — 解释

原书《从 SEO 到 GEO》聚焦国产引擎的内容与渠道打法；本卡补充"官网能不能被 AI 爬虫正常取用"这一更底层的前提——**页面进不了候选集，一切可引用性优化都不起作用**。

**一、AI 爬虫按用途分三类，放行策略必须按类决策（不能按名字一刀切）：**

| 类别 | 代表爬虫 | 屏蔽后果 |
|---|---|---|
| 训练类 | GPTBot、ClaudeBot、Google-Extended、CCBot、Bytespider（字节）等 | 失去进入未来模型"参数记忆"的机会，但**保留被引用可能** |
| 检索类 | OAI-SearchBot、PerplexityBot、Claude-SearchBot、Googlebot（AI Overviews）、Bingbot（Copilot） | **立即失去被引用机会**，而训练大多已发生或另有语料——屏蔽检索类是代价最高的错误 |
| 用户触发类 | ChatGPT-User、Claude-User、Perplexity-User | 仅该用户此刻对这一页的实时查询失败 |

常见反模式：为了拦训练类在 robots.txt 里把 AI 爬虫全部 Disallow——同时屏蔽了检索类，自断被引通道。另两条纪律：robots.txt 是声明不是强制（RFC 9309，依赖自愿遵守，硬限制需网络层手段）；UA 字符串由客户端自报、易伪造，核验身份要用"运营方公布的 IP 段 + 前向确认反向解析（FCrDNS）"。

**二、llms.txt：低成本预先部署，但不要指望它直接带来引用。** Answer.AI 2024-09 提出的发布约定：在站点根目录放 `/llms.txt`，一份筛选过的 Markdown 索引（H1 项目名 + blockquote 摘要 + `##` 分节链接列表 + Optional 低优先节）。三条诚实边界：截至 2026-05 无任何主流厂商文档说明其爬虫会读取它（Anthropic/Google/Perplexity 在自家文档站托管 llms.txt ≠ 其爬虫会读你的）；它不是标准（未过 IETF/W3C）；与 robots.txt（访问控制）、sitemap.xml（完整发现覆盖）职责不重叠、不可互替——llms.txt 只负责"筛选与简洁呈现"。结论：部署成本约等于零、向前兼容，值得做；把它当引用手段则是误判。

**补充（GeoLook 六维体检方法，MIT，框架采用 GeoReady《The GEO Readiness Manual》）——四层依赖模型决定修复顺序：访问 → 定向 → 理解 → 可引用**，每层依赖上一层，**先修失败的最上游层**：访问层（robots 封禁/WAF-UA 差异封锁/noindex/SPA 空壳）失败时，下游的 schema 和内容优化在引擎侧全部不可见。三个国内官网高频致命点：①**SPA 空壳页**（正文 word_count≈0，AI 抓取器看到的是空白）；②**WAF/CDN 按 UA 拦截**——robots.txt 放行但换 AI 爬虫 UA 实测被 CDN 403，浏览器里看不出来，必须换真实 AI UA 探测；③**X-Robots-Tag 头级 noindex**——页面源码里看不到，要查响应头。

**补充四（GEO Wiki ai-crawlers 全文 + GeoLook method + geo-seo-claude，2026-09-14 穷尽审查）——放行策略的关键纠错与细则：**

1. **Bytespider（字节跳动）实测不遵守 robots.txt 且无官方文档**（GEO Wiki 令牌表）——对它，robots.txt 只是姿态，硬限制只能走网络层（WAF/IP 段）。
2. **令牌按产品核对，不能照搬经验**（三个官方实例）：屏蔽 GPTBot 不影响 ChatGPT 搜索可见性（那由 OAI-SearchBot + ChatGPT-User 决定）；Google 官方原文确认 Google-Extended 与搜索收录/排名无关、AIO 无专属爬虫（退出 AIO 只有退出 Google 搜索一条路）；同一个 Google-Extended 令牌对 AIO 无效、却控制 Gemini Apps/Vertex 的 grounding 采信。
3. **Extended 令牌不是真实 UA**：Google-Extended / Applebot-Extended 是 robots.txt 控制令牌，实际抓取由 Googlebot/Applebot 完成——robots 判断与边缘测试分开处理。
4. **26 个令牌全名单**（GEO Wiki 2026-08-18 核验，超出"代表 UA"的完整版）：训练类含 GPTBot、ClaudeBot、Google-Extended、Applebot-Extended、CCBot、meta-externalagent、Amazonbot、MistralAI-Training、AI2Bot、Bytespider；检索类含 OAI-SearchBot、Claude-SearchBot、PerplexityBot、Googlebot、bingbot、Applebot、DuckAssistBot、YouBot、MistralAI-Index；用户触发类含 ChatGPT-User、Claude-User、Perplexity-User、meta-externalfetcher、MistralAI-User、Google-GeminiNotebook、Google-Agent。每季度复查——固定白名单会让新出现的爬虫默认被排除。
5. **分爬虫 JS 渲染差异**：Googlebot 会渲染但有延迟队列（可延迟数天数周）；GPTBot/ClaudeBot/PerplexityBot 按纯 HTML 对待——SPA 空壳对这些爬虫等于不存在。
6. **robots.txt 要按 RFC 9309 语义判**（GeoLook）：逐行正则会漏三种真实封禁——`User-agent: * / Disallow: /` 通配符组封掉所有无专属组的 AI 爬虫（最常见的"无意封禁"）；多 UA 共享规则组；specificity 规则不看顺序（存在专属组时通配符组整组失效）。
7. **头部与元标记**：X-Robots-Tag 响应头覆盖 meta 且适用于非 HTML 资源（图片/PDF 也会被 noindex）；另有 bot 专属 meta（如 `<meta name="GPTBot" content="noindex">`）。
8. **屏蔽面统计**：Top 1000 网站 35%+ 屏蔽至少一只 AI 爬虫、5-10% 全屏蔽（Originality.ai 2025）——大多数站点没做"按类放行"这一步。
9. **新兴方向（B 段级，不能依赖）**：IETF draft 的 Web Bot Auth（HTTP 消息签名验证爬虫身份）；robots.txt 的 Content-Signal 指令（`ai-train=no, search=yes, ai-retrieval=yes`，IETF draft）；ai.txt 提案标准；IndexNow（/.well-known/indexnow-key.txt + 发布时 ping API——ChatGPT 走 Bing 索引，加速 Bing 即加速 ChatGPT 收录）；Agent-Readiness Link 头与 `Accept: text/markdown` 内容协商（Cloudflare "Markdown for Agents"）。
10. **页面深度**：4 层以上深度的页面爬行预算骤减，更难被 AI 引用——重要页面别埋深。

**补充五（llms.txt 工程细则，GEO Wiki llms-txt + geo-seo-claude geo-llmstxt）：**

- **纠错**：llms-full.txt 不在原始规范（Mintlify 推广形成的约定）；规范定义的是 llms-ctx.txt / llms-ctx-full.txt（llms_txt2ctx 生成）。**Google 已书面表示其 AI 功能不会使用 llms.txt**——比"无厂商确认"更强一档。90 天 × 10 站点研究结论：当 sitemap 类基础设施，不是增长手段。
- **硬格式**：根路径（v2 起可用子路径 + head 内 `<link rel="describedby" href="/llms.txt">` 声明）；H1 首行、blockquote 摘要 <200 字符、总条目 10-30、每条目 10-30 词描述、绝对 URL。
- **收录三档**：收录高价值页（定价/核心文档/FAQ）→ 可选收录次要页 → **跳过**：薄分类/标签页、分页、登录注册页、法律样板。
- **误用清单（弊大于利）**：内容陈旧的 llms.txt 比没有更糟；把整个 sitemap 塞进去失去筛选意义；必须由构建过程自动生成并保持同步；所列页面**不得被 robots.txt 对 AI 爬虫屏蔽**（自相矛盾）；部署后验证无重定向。
- **质量分参考**：完整性 40% + 准确性 35% + 有用性 25%（geo-seo-claude 口径）；验证严重级——H1 与至少一个 H2 为 Critical。

## A1 — 案例（补充来源，非原书案例）

- **原书未提供案例**（如实标注）。GEO Wiki 给出的可核验事实：一项覆盖 30 万域名的研究测得约 10% 域名已部署 llms.txt（SEJ，2025-11）；Cloudflare 发现仅约 14% 的 robots.txt 专门设置 AI 爬虫规则（2025-07），多数站点尚未声明任何策略——多数站点连"按类放行"这一步都没做。

## A2 — 未来触发

- 用户问"要不要屏蔽 GPTBot/Bytespider/爬虫 / robots.txt 该怎么写 AI 规则 / 网站内容怎么让 AI 抓到"。
- 用户问"llms.txt 是什么、要不要做、和 sitemap/robots.txt 什么关系"。
- 用户怀疑"AI 引擎根本抓不到我的网站/渲染后才有内容"。
- 语言信号：robots.txt、GPTBot、Bytespider、AI 爬虫、屏蔽、llms.txt、抓取、SSR、爬虫访问 / ai crawler, robots.txt, llms.txt, block GPTBot。
- 与相邻能力区分：本卡管"能不能被抓到"（候选集入口）；内容写得能不能被引用归 citable-content-spec；官网事实页与结构化数据基建归 brand-data-infrastructure（本卡与它互补：先可抓取，再谈事实页）。

## E — 执行步骤

输入契约：站点 robots.txt 现状；渲染方式（SSR/CSR）；是否已有 llms.txt/sitemap.xml。缺 robots.txt 内容先索取。

1. **审计四状态**（改编自 GEO Wiki《AI 爬虫访问审计》）：你决定放行哪些类 → robots.txt 对外声明了什么 → 真实请求返回什么 → 日志里谁的到访。发现几乎都来自相邻状态不一致。
2. **按类决策放行策略**：检索类+用户触发类默认放行（这是被引用的前提）；训练类按业务自定（放行换"参数记忆"，屏蔽换控制）；逐类写 robots.txt 规则，禁止"AI 爬虫全部 Disallow"的一刀切。
3. **核验可读性**：重要内容必须在渲染后的 HTML 中可直接读取（CSR 站点做 SSR/预渲染兜底）；用 geo.wiki 免费工具自检（AI 爬虫访问检测 https://geo.wiki/zh/tools/ai-crawler-access 、Schema 标记检测 /zh/tools/schema-check）。
4. **部署 llms.txt（可选，≤1 天投入）**：筛选 10–30 个应优先读取的页面 → 按规范写 /llms.txt（H1+摘要+分节链接）→ 列出的每个 URL 提供干净 Markdown 版 → 无人维护就删除。
5. **输出**：robots.txt 修改建议（按类逐条）+ 可读性问题清单 + llms.txt 文件（如做）。完成标准：检索类爬虫在 robots.txt 与真实响应两层都被放行。

## B — 边界

- **证据时效**：爬虫名单变化很快（GEO Wiki 明示每次复审需对照官方文档重核）；llms.txt 的"引擎是否读取"截至 2026-05 未获任何厂商确认，Google 的 John Mueller 公开质疑过它——部署它只押"向前兼容"，不押当下引用。
- robots.txt 无法阻止不合规爬虫（有公开报道记录过答案引擎无视禁抓、爬虫伪装浏览器轮换 IP）；硬需求走网络层（WAF/已核验名单）。
- 国内引擎的抓取行为（哪些 UA 在抓）暂无系统实测，本卡的爬虫名单以海外引擎官方文档为主；Bytespider（字节）与豆包生态的对应关系未经验证。
- 屏蔽训练类 ≠ 隐私合规工具；敏感数据保护要走单独的合规路径。

## 相关能力

上游前提于 brand-data-infrastructure（层 1 结构化数据）与 aeo-answer-optimization（机器可读形态）；被 geo-monitoring-iteration 的"整个 query 无引用"分支调用（排查候选集入口）。
