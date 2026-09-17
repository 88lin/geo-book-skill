# -*- coding: utf-8 -*-
"""一次性生成 geo-playbook/resources 下的国内口径 JSON-LD 模板。"""
import io, json, glob, collections, os

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "geo-playbook", "resources"))

def W(name, obj):
    io.open(name, "w", encoding="utf-8", newline="\n").write(
        json.dumps(obj, ensure_ascii=False, indent=2) + "\n")

D = "https://YOURDOMAIN.com"
OD = collections.OrderedDict

W("schema-organization.json", OD([
    ("@context", "https://schema.org"), ("@type", "Organization"), ("@id", D + "/#organization"),
    ("name", "品牌全称（与营业执照一致）"), ("alternateName", "品牌常用简称"), ("url", D),
    ("logo", {"@type": "ImageObject", "url": D + "/logo.png", "width": 600, "height": 60}),
    ("description", "一句话说清你是谁、为谁解决什么问题（40-60 字，与官网首屏首段逐字一致）"),
    ("foundingDate", "YYYY-MM-DD"),
    ("founder", {"@type": "Person", "name": "创始人姓名", "url": D + "/about/founder",
                 "sameAs": ["https://www.zhihu.com/people/ZHIHU_ID", "https://weibo.com/WEIBO_ID"]}),
    ("contactPoint", [
        {"@type": "ContactPoint", "telephone": "+86-400-XXX-XXXX", "contactType": "customer service",
         "email": "support@YOURDOMAIN.com", "availableLanguage": ["zh-CN"],
         "hoursAvailable": {"@type": "OpeningHoursSpecification",
                            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                            "opens": "09:00", "closes": "18:00"}},
        {"@type": "ContactPoint", "telephone": "+86-XXX-XXXX-XXXX", "contactType": "sales",
         "email": "sales@YOURDOMAIN.com", "availableLanguage": ["zh-CN"]}]),
    ("address", {"@type": "PostalAddress", "streetAddress": "XX 区 XX 路 XX 号 XX 座 XX 室",
                 "addressLocality": "城市（如：杭州市）", "addressRegion": "省/直辖市（如：浙江省）",
                 "postalCode": "XXXXXX", "addressCountry": "CN"}),
    ("sameAs", ["https://www.zhihu.com/org/YOUR_ZHIHU",
                "https://weibo.com/YOUR_WEIBO",
                "https://baike.baidu.com/item/YOUR_BAIKE",
                "https://space.bilibili.com/YOUR_BILIBILI",
                "https://www.xiaohongshu.com/user/profile/YOUR_XHS",
                "https://www.douyin.com/user/YOUR_DOUYIN",
                "https://www.qcc.com/firm/YOUR_QCC.html",
                "https://gitee.com/YOUR_GITEE",
                "https://github.com/YOUR_GITHUB",
                "https://www.wikidata.org/wiki/YOUR_WIKIDATA_ID"]),
    ("numberOfEmployees", {"@type": "QuantitativeValue", "value": "XX"}),
    ("areaServed", {"@type": "Country", "name": "CN"}),
    ("knowsAbout", ["主营领域 1", "主营领域 2", "主营领域 3"]),
    ("inLanguage", "zh-CN")]))

W("schema-software-saas.json", OD([
    ("@context", "https://schema.org"), ("@type", "SoftwareApplication"), ("@id", D + "/#software"),
    ("name", "产品名称"), ("url", D),
    ("description", "一句话说清产品是什么、给谁用、解决什么问题（40-60 字）"),
    ("applicationCategory", "BusinessApplication"),
    ("operatingSystem", "Web, Windows, macOS, Android, iOS"),
    ("offers", OD([("@type", "AggregateOffer"), ("lowPrice", "XXXX"), ("highPrice", "XXXXX"),
                   ("priceCurrency", "CNY"), ("offerCount", "3"),
                   ("offers", [
                       {"@type": "Offer", "name": "基础版", "price": "XXXX", "priceCurrency": "CNY",
                        "priceValidUntil": "YYYY-12-31", "availability": "https://schema.org/InStock",
                        "description": "年费 XXXX 元/年，含 X 个坐席；抽佣与手续费另计，三笔账分开列"},
                       {"@type": "Offer", "name": "专业版", "price": "XXXXX", "priceCurrency": "CNY",
                        "priceValidUntil": "YYYY-12-31", "availability": "https://schema.org/InStock"},
                       {"@type": "Offer", "name": "旗舰版", "price": "XXXXX", "priceCurrency": "CNY",
                        "priceValidUntil": "YYYY-12-31", "availability": "https://schema.org/InStock"}])])),
    ("featureList", ["核心能力 1", "核心能力 2", "核心能力 3", "核心能力 4"]),
    ("screenshot", D + "/images/screenshot.png"),
    ("softwareVersion", "X.X"), ("releaseNotes", D + "/changelog"),
    ("author", {"@type": "Organization", "@id": D + "/#organization"}),
    ("sameAs", ["https://www.zhihu.com/org/YOUR_ZHIHU",
                "https://gitee.com/YOUR_GITEE",
                "https://github.com/YOUR_GITHUB",
                "https://juejin.cn/user/YOUR_JUEJIN",
                "https://blog.csdn.net/YOUR_CSDN",
                "https://www.qcc.com/firm/YOUR_QCC.html"]),
    ("inLanguage", "zh-CN")]))

W("schema-product-ecommerce.json", OD([
    ("@context", "https://schema.org"), ("@type", "Product"),
    ("@id", D + "/products/PRODUCT_SLUG/#product"),
    ("name", "商品名称"), ("url", D + "/products/PRODUCT_SLUG"),
    ("description", "商品一句话卖点 + 适用人群（40-60 字）"),
    ("image", [D + "/images/products/PRODUCT_1.jpg", D + "/images/products/PRODUCT_2.jpg",
               D + "/images/products/PRODUCT_3.jpg"]),
    ("brand", {"@type": "Brand", "name": "品牌名"}),
    ("sku", "YOUR_SKU"), ("gtin13", "商品条码 13 位"), ("mpn", "厂商型号"),
    ("category", "商品类目"), ("material", "材质"), ("color", "颜色"),
    ("weight", {"@type": "QuantitativeValue", "value": "X.X", "unitCode": "KGM"}),
    ("offers", OD([("@type", "Offer"), ("url", D + "/products/PRODUCT_SLUG"),
                   ("price", "XXX.XX"), ("priceCurrency", "CNY"),
                   ("priceValidUntil", "YYYY-12-31"),
                   ("availability", "https://schema.org/InStock"),
                   ("itemCondition", "https://schema.org/NewCondition"),
                   ("seller", {"@type": "Organization", "@id": D + "/#organization"}),
                   ("shippingDetails", {"@type": "OfferShippingDetails",
                                        "shippingRate": {"@type": "MonetaryAmount", "value": "0", "currency": "CNY"},
                                        "deliveryTime": {"@type": "ShippingDeliveryTime",
                                                         "handlingTime": {"@type": "QuantitativeValue", "minValue": "0", "maxValue": "1", "unitCode": "DAY"},
                                                         "transitTime": {"@type": "QuantitativeValue", "minValue": "1", "maxValue": "3", "unitCode": "DAY"}},
                                        "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "CN"}}),
                   ("hasMerchantReturnPolicy", {"@type": "MerchantReturnPolicy", "applicableCountry": "CN",
                                                "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
                                                "merchantReturnDays": "7",
                                                "returnMethod": "https://schema.org/ReturnByMail",
                                                "returnFees": "https://schema.org/FreeReturn"})])),
    # 评分必须来自真实平台数据，占位符刻意写成不可能通过校验的形式：
    # 填不上就整块删掉，绝不能留着假分上线（伪造评价是本技能的红线）
    ("aggregateRating", {"@type": "AggregateRating", "ratingValue": "X.X", "reviewCount": "XXX",
                         "bestRating": "5", "worstRating": "1"}),
    ("review", [{"@type": "Review", "author": {"@type": "Person", "name": "真实买家昵称"},
                 "datePublished": "YYYY-MM-DD",
                 "reviewRating": {"@type": "Rating", "ratingValue": "X", "bestRating": "5"},
                 "reviewBody": "真实评价原文，不得编造或批量生成"}]),
    ("inLanguage", "zh-CN")]))

W("schema-local-business.json", OD([
    ("@context", "https://schema.org"), ("@type", "LocalBusiness"), ("@id", D + "/#localbusiness"),
    ("name", "门店名（与高德/百度地图/点评逐字一致，含括号后缀写法）"),
    ("url", D), ("image", D + "/images/storefront.jpg"),
    ("description", "门店一句话介绍：卖什么 + 商圈位置"),
    ("telephone", "+86-XXX-XXXX-XXXX"), ("email", "contact@YOURDOMAIN.com"),
    ("priceRange", "¥XX-XXX"), ("currenciesAccepted", "CNY"),
    ("paymentAccepted", "微信支付, 支付宝, 现金, 银行卡"),
    ("address", {"@type": "PostalAddress", "streetAddress": "XX 区 XX 路 XX 号（与各平台一字不差）",
                 "addressLocality": "城市（如：杭州市）", "addressRegion": "省/直辖市（如：浙江省）",
                 "postalCode": "XXXXXX", "addressCountry": "CN"}),
    ("geo", {"@type": "GeoCoordinates", "latitude": "XX.XXXXXX", "longitude": "XXX.XXXXXX"}),
    ("openingHoursSpecification", [
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
         "opens": "09:00", "closes": "18:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday", "Sunday"],
         "opens": "10:00", "closes": "20:00"}]),
    ("areaServed", {"@type": "GeoCircle",
                    "geoMidpoint": {"@type": "GeoCoordinates", "latitude": "XX.XXXXXX", "longitude": "XXX.XXXXXX"},
                    "geoRadius": "5000"}),
    ("sameAs", ["https://www.amap.com/place/YOUR_AMAP_POI",
                "https://map.baidu.com/poi/YOUR_BAIDU_POI",
                "https://www.dianping.com/shop/YOUR_DIANPING_ID",
                "https://meituan.com/YOUR_MEITUAN",
                "https://www.douyin.com/user/YOUR_DOUYIN",
                "https://www.xiaohongshu.com/user/profile/YOUR_XHS"]),
    # 同上：真实评分才填，填不上整块删除
    ("aggregateRating", {"@type": "AggregateRating", "ratingValue": "X.X", "reviewCount": "XX",
                         "bestRating": "5"}),
    ("hasOfferCatalog", {"@type": "OfferCatalog", "name": "服务项目", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "服务 1", "description": "服务 1 说明"},
         "price": "XXX", "priceCurrency": "CNY"},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "服务 2", "description": "服务 2 说明"},
         "price": "XXX", "priceCurrency": "CNY"}]}),
    ("inLanguage", "zh-CN")]))

W("schema-article-author.json", OD([
    ("@context", "https://schema.org"), ("@type", "Article"),
    ("@id", D + "/blog/ARTICLE_SLUG/#article"),
    ("headline", "标题：直接用目标 query 的用户原话，可带更新日期"),
    ("description", "首段 40-60 字结论，与页面可见首屏逐字一致"),
    ("url", D + "/blog/ARTICLE_SLUG"),
    ("datePublished", "YYYY-MM-DD"), ("dateModified", "YYYY-MM-DD"),
    ("image", {"@type": "ImageObject", "url": D + "/images/ARTICLE_IMAGE.jpg", "width": 1200, "height": 630}),
    ("author", OD([("@type", "Person"), ("@id", D + "/about/AUTHOR_SLUG/#person"),
                   ("name", "作者真名或可核实的固定笔名"),
                   ("url", D + "/about/AUTHOR_SLUG"),
                   ("image", D + "/images/authors/AUTHOR_IMAGE.jpg"),
                   ("jobTitle", "职位"),
                   ("description", "一句话资历：做过什么、多少年、可核实的成果"),
                   ("knowsAbout", ["专长 1", "专长 2", "专长 3"]),
                   ("sameAs", ["https://www.zhihu.com/people/AUTHOR_ZHIHU",
                               "https://weibo.com/AUTHOR_WEIBO",
                               "https://juejin.cn/user/AUTHOR_JUEJIN",
                               "https://blog.csdn.net/AUTHOR_CSDN",
                               "https://github.com/AUTHOR_GITHUB"]),
                   ("alumniOf", {"@type": "CollegeOrUniversity", "name": "毕业院校"}),
                   ("worksFor", {"@type": "Organization", "name": "所属机构", "@id": D + "/#organization"})])),
    ("publisher", {"@type": "Organization", "@id": D + "/#organization", "name": "品牌全称",
                   "logo": {"@type": "ImageObject", "url": D + "/logo.png"}}),
    ("mainEntityOfPage", {"@type": "WebPage", "@id": D + "/blog/ARTICLE_SLUG"}),
    ("wordCount", "XXXX"), ("articleSection", "栏目"),
    ("keywords", "关键词 1, 关键词 2, 关键词 3"),
    ("citation", ["引用的权威来源标题与链接 1", "引用的权威来源标题与链接 2"]),
    ("speakable", {"@type": "SpeakableSpecification",
                   "cssSelector": [".article-summary", ".key-takeaway", "h2"]}),
    ("isAccessibleForFree", True),
    ("inLanguage", "zh-CN")]))

W("schema-website-searchaction.json", OD([
    ("@context", "https://schema.org"), ("@type", "WebSite"), ("@id", D + "/#website"),
    ("name", "站点名"), ("url", D), ("description", "站点一句话介绍"),
    ("publisher", {"@type": "Organization", "@id": D + "/#organization"}),
    ("potentialAction", {"@type": "SearchAction",
                         "target": {"@type": "EntryPoint", "urlTemplate": D + "/search?q={search_term_string}"},
                         "query-input": "required name=search_term_string"}),
    ("inLanguage", "zh-CN")]))

W("schema-faqpage.json", OD([
    ("@context", "https://schema.org"), ("@type", "FAQPage"),
    ("@id", D + "/faq/PAGE_SLUG/#faqpage"), ("url", D + "/faq/PAGE_SLUG"),
    ("isPartOf", {"@type": "WebSite", "@id": D + "/#website"}),
    ("publisher", {"@type": "Organization", "@id": D + "/#organization"}),
    ("dateModified", "YYYY-MM-DD"),
    ("mainEntity", [
        {"@type": "Question", "name": "问题一：用目标 query 的用户原话，不要改写成品牌内部叫法",
         "acceptedAnswer": {"@type": "Answer",
                            "text": "第一句直接给结论（40-60 字），再展开条件与例外；带日期的数字写在正文里。本段必须与页面可见文字逐字一致。"}},
        {"@type": "Question", "name": "问题二：用户原话",
         "acceptedAnswer": {"@type": "Answer", "text": "可独立摘引的短答案：结论 + 数字 + 适用边界。"}},
        {"@type": "Question", "name": "问题三：用户原话",
         "acceptedAnswer": {"@type": "Answer", "text": "可独立摘引的短答案：结论 + 数字 + 适用边界。"}}]),
    ("inLanguage", "zh-CN")]))

W("schema-howto.json", OD([
    ("@context", "https://schema.org"), ("@type", "HowTo"),
    ("@id", D + "/guides/GUIDE_SLUG/#howto"),
    ("name", "怎么做 XXX：用症状原句作标题"),
    ("description", "首段 40-60 字结论：这套步骤解决什么问题、大概多久、需要什么前提"),
    ("url", D + "/guides/GUIDE_SLUG"), ("image", D + "/images/GUIDE_IMAGE.jpg"),
    ("datePublished", "YYYY-MM-DD"), ("dateModified", "YYYY-MM-DD"),
    ("totalTime", "PT30M"),
    ("estimatedCost", {"@type": "MonetaryAmount", "currency": "CNY", "value": "XXX"}),
    ("supply", [{"@type": "HowToSupply", "name": "需要准备的材料/账号 1"}]),
    ("tool", [{"@type": "HowToTool", "name": "需要用到的工具 1"}]),
    ("step", [
        {"@type": "HowToStep", "position": 1, "name": "第一步标题（动词开头）",
         "text": "这一步具体做什么、判断阈值是多少、什么情况下停下来。", "url": D + "/guides/GUIDE_SLUG#step1"},
        {"@type": "HowToStep", "position": 2, "name": "第二步标题",
         "text": "步骤正文，含具体数值与红线。", "url": D + "/guides/GUIDE_SLUG#step2"},
        {"@type": "HowToStep", "position": 3, "name": "第三步标题",
         "text": "步骤正文，含完成标准。", "url": D + "/guides/GUIDE_SLUG#step3"}]),
    ("author", {"@type": "Organization", "@id": D + "/#organization"}),
    ("inLanguage", "zh-CN")]))

W("schema-breadcrumb.json", OD([
    ("@context", "https://schema.org"), ("@type", "BreadcrumbList"),
    ("@id", D + "/CURRENT_PAGE/#breadcrumb"),
    ("itemListElement", [
        {"@type": "ListItem", "position": 1, "name": "首页", "item": D},
        {"@type": "ListItem", "position": 2, "name": "栏目名", "item": D + "/SECTION"},
        {"@type": "ListItem", "position": 3, "name": "当前页标题", "item": D + "/SECTION/CURRENT_PAGE"}])]))

files = sorted(glob.glob("*.json"))
for f in files:
    json.load(io.open(f, encoding="utf-8"))
print("wrote & validated %d JSON-LD templates: %s" % (len(files), ", ".join(files)))
