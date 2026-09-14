# 回归评测：ai-crawler-access

## 评测问题

> "我们是一个中文 SaaS 官网，想让 AI 搜索引擎能抓到我们。现在的状况是：robots.txt 里写了 `User-agent: * / Disallow: /`，前端是 React SPA，没有 llms.txt。请帮我审查问题并给出修复方案。另外，我听说有个 llms-full.txt，要不要也部署？"

## 回答

你们现在有三个层面的问题，按修复优先级从上游到下游排：**访问层（robots.txt 全封）→ 可读层（SPA 空壳）→ 定向层（缺 llms.txt）**。访问层不修通，后面两层在引擎侧全部不可见，所以先从 robots.txt 开始。

### 一、robots.txt：`User-agent: * / Disallow: /` 是最典型的"无意封禁"

这条规则的意思是"对所有未声明专属组的爬虫，禁止抓取全站"。按 RFC 9309 的语义，通配符组会封掉所有没有专属 `User-agent` 组的爬虫——也就是说，你们现在把三类 AI 爬虫全挡在外面了：

- **检索类**（OAI-SearchBot、PerplexityBot、Claude-SearchBot、Googlebot、bingbot、Applebot、DuckAssistBot、YouBot、MistralAI-Index 等）：被屏蔽的后果最严重——内容立即不再出现在 AI 答案中。这是代价最高的错误。
- **用户触发类**（ChatGPT-User、Claude-User、Perplexity-User、meta-externalfetcher、MistralAI-User、Google-GeminiNotebook、Google-Agent 等）：该用户此刻的实时查询失败。
- **训练类**（GPTBot、ClaudeBot、Google-Extended、Applebot-Extended、CCBot、meta-externalagent、Amazonbot、MistralAI-Training、AI2Bot、Bytespider 等）：失去进入未来模型"参数记忆"的机会，但被引用的通道还在。

**修复方案——按类决策，逐类写规则，禁止一刀切：**

1. 检索类 + 用户触发类：默认放行（这是被引用的前提）。
2. 训练类：按你们业务意愿决定。放行 = 换取进入模型参数记忆的机会；屏蔽 = 控制语料被用于训练，但保留被引用可能。
3. 写法示例（假设你们决定检索类、用户触发类、训练类都放行）：

```
# 检索类 —— 放行
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Googlebot
Allow: /

User-agent: bingbot
Allow: /

# 用户触发类 —— 放行
User-agent: ChatGPT-User
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Perplexity-User
Allow: /

# 训练类 —— 按需
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

# 通配符兜底
User-agent: *
Disallow:
```

几个关键纠错点：

- **按产品核对令牌，不能照搬经验**。屏蔽 GPTBot 不影响 ChatGPT 搜索可见性——那由 OAI-SearchBot + ChatGPT-User 决定；Google-Extended 与搜索收录/排名无关，AIO（AI Overviews）没有专属爬虫，退出 AIO 只有退出 Google 搜索一条路；同一个 Google-Extended 令牌对 AIO 无效，却控制 Gemini Apps/Vertex 的 grounding 采信。
- **Extended 令牌不是真实 UA**。Google-Extended / Applebot-Extended 是 robots.txt 控制令牌，实际抓取由 Googlebot / Applebot 完成——robots 判断和边缘测试要分开处理。
- **Bytespider（字节跳动）实测不遵守 robots.txt 且无官方文档**。对它，robots.txt 只是姿态，真要硬限制只能走网络层（WAF / IP 段）。
- **robots.txt 是声明不是强制**。UA 字符串由客户端自报、易伪造，核验身份要用"运营方公布的 IP 段 + 前向确认反向解析（FCrDNS）"。
- **每季度复查令牌名单**。固定白名单会让新出现的爬虫默认被排除。

### 二、React SPA 空壳：对多数 AI 爬虫等于不存在

SPA 的正文在客户端 JS 执行后才渲染，AI 爬虫抓到的初始 HTML 里 `word_count ≈ 0`——看到的是空白。各爬虫的 JS 渲染能力差异很大：

- **Googlebot** 会渲染，但有延迟队列，可能延迟数天甚至数周。
- **GPTBot / ClaudeBot / PerplexityBot 按纯 HTML 对待**——SPA 空壳对这些爬虫等于页面不存在。

**修复方案：**

1. 对重要内容页做 **SSR 或预渲染兜底**，保证渲染后的 HTML 中可直接读取正文。Next.js 的 SSG/SSR、或预渲染服务（Prerender.io 等）都可以。
2. 用工具自检：可以用 geo.wiki 的免费 AI 爬虫访问检测工具（https://geo.wiki/zh/tools/ai-crawler-access ）换真实 AI UA 探测，看抓到的 HTML 是否有正文。
3. 另外两个高频隐蔽问题也一并排查：
   - **WAF/CDN 按 UA 拦截**：robots.txt 放行了但换 AI 爬虫 UA 实测被 CDN 返回 403——浏览器里看不出来，必须换真实 AI UA 探测才能发现。
   - **X-Robots-Tag 响应头级 noindex**：页面源码里看不到，要查 HTTP 响应头；这个头对非 HTML 资源（图片/PDF）也生效。

### 三、llms.txt：值得部署，但别当引用手段

llms.txt 是 Answer.AI 2024-09 提出的发布约定：在站点根目录放一份筛选过的 Markdown 索引。部署成本约等于零、向前兼容，值得做；但要诚实看待它的边界：

- 截至 2026-05，**无任何主流厂商文档说明其爬虫会读取它**。Google 已书面表示其 AI 功能不会使用 llms.txt——这比"无厂商确认"更强一档。
- 它不是标准（未过 IETF/W3C），与 robots.txt（访问控制）、sitemap.xml（完整发现）职责不重叠、不可互替——llms.txt 只负责"筛选与简洁呈现"。
- 90 天 × 10 站点研究结论：当 sitemap 类基础设施用，不是增长手段。

**部署建议（≤1 天投入）：**

1. 筛选 10–30 个应优先读取的页面：定价页、核心文档、FAQ 等高价值页。
2. 按硬格式写 `/llms.txt`：
   - H1 首行写项目名
   - 紧跟一个 blockquote 摘要（< 200 字符）
   - `##` 分节 + 链接列表，每条目描述 10–30 词，用绝对 URL
   - 总条目 10–30
3. 收录三档：高价值页收录 → 次要页可选收录 → **跳过**薄分类/标签页、分页、登录注册页、法律样板。
4. **必须由构建过程自动生成并保持同步**——内容陈旧的 llms.txt 比没有更糟。
5. **所列页面不得被 robots.txt 对 AI 爬虫屏蔽**（否则自相矛盾）。
6. 部署后验证无重定向。
7. v2 起可用子路径 + 在 head 内加 `<link rel="describedby" href="/llms.txt">` 声明。
8. 不要把整个 sitemap 塞进去——失去筛选意义。

### 四、llms-full.txt：不在原始规范，不建议部署

你听说的 llms-full.txt **不在原始规范**里——它是 Mintlify 推广形成的约定。规范定义的扩展文件是 `llms-ctx.txt` / `llms-ctx-full.txt`（由 llms_txt2ctx 生成）。所以 llms-full.txt 不需要部署；如果未来需要给 LLM 提供完整上下文，走 llms-ctx 系列才是规范路径。

### 修复优先级总结

1. **先修 robots.txt**（访问层）——把检索类和用户触发类放行，这是被引用的前提。
2. **再修 SPA 空壳**（可读层）——做 SSR/预渲染，保证 AI 爬虫抓到的 HTML 有正文。
3. **然后部署 llms.txt**（定向层）——低成本向前兼容，但不是引用手段。
4. **llms-full.txt 不部署**——不在规范内。
5. 全程用真实 AI UA 探测验证，不要只看浏览器效果。

## 自评

| 维度 | 得分 | 说明 |
|---|---|---|
| 覆盖度 | 9/10 | 覆盖了卡片中所有与该问题直接相关的知识点：robots.txt 按类放行（三类完整列举）、SPA 空壳问题（含 JS 渲染差异）、llms.txt 部署建议（格式/收录三档/误用清单）、llms-full.txt 纠错、Bytespider 特殊性、WAF/CDN UA 拦截、X-Robots-Tag、Extended 令牌非真实 UA、按产品核对令牌、四层依赖模型修复顺序。未展开 IndexNow、页面深度等与该问题关联较弱的知识点，扣 1 分。 |
| 准确度 | 10/10 | 所有事实均来自卡片内容，无编造。26 令牌全名单按训练/检索/用户触发三类准确分类；llms-full.txt 纠错（Mintlify 约定 vs 规范的 llms-ctx）与卡片一致；Bytespider 不遵守 robots.txt 的表述与卡片一致；Google 已书面表示不使用 llms.txt 的表述与卡片一致；RFC 9309 通配符组语义与卡片一致。 |
| 可操作性 | 9/10 | 给出了可直接使用的 robots.txt 示例配置、SSR/预渲染具体方案（Next.js SSG/SSR、Prerender.io）、llms.txt 逐步部署清单（8 步）、明确的修复优先级排序、可用的自检工具 URL。扣 1 分因 robots.txt 示例未覆盖全部 26 个令牌（为可读性做了精简，但客户可能需要完整版）。 |
| 补充块利用率 | 10/10 | 充分利用了 v0.4.2 补充块内容：补充四的 26 令牌全名单（三类完整列出）、RFC 9309 语义（通配符组封禁机制）、Bytespider 不遵守 robots.txt、Extended 令牌非真实 UA、按产品核对令牌（三个官方实例）、JS 渲染差异（Googlebot 延迟队列 vs 纯 HTML）、WAF/CDN 与 X-Robots-Tag 隐蔽问题；补充五的 llms-full.txt 纠错、Google 书面表态、硬格式规范、收录三档、误用清单、llms-ctx 规范路径；补充块的四层依赖模型用于修复优先级排序。 |
| **总分** | **38/40** | |

## 结论

PASS（38/40 ≥ 28/40）
