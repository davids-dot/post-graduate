import scrapy


class SoftwareEngineerCrawler(scrapy.Spider):
    name = "software_engineer_crawler"
    allowed_domains = ["yz.chsi.com.cn"]
    start_urls = ["https://yz.chsi.com.cn/zsml/a/zydetail.do?zydm=085405&zymc=%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B&xwlx=zyxw&mldm=08&mlmc=%E5%B7%A5%E5%AD%A6&yjxkdm=0854&yjxkmc=%E7%94%B5%E5%AD%90%E4%BF%A1%E6%81%AF&xxfs=&tydxs=&jsggjh=&sign=c5e9fff84148866d650fc3379f8def13"]

    def start_requests(self):
        cookies = [
            {
                "domain": "yz.chsi.com.cn",
                "name": "JSESSIONID",
                "path": "/zsml",
                "sameSite": "unspecified",
                "storeId": "0",
                "value": "B390F4A9D5AFC1853C9F755AA6A78C67"
            },
            {
                "domain": "yz.chsi.com.cn",
                "name": "CHSICC_CLIENTFLAGYZ",
                "path": "/",
                "sameSite": "unspecified",
                "storeId": "0",
                "value": "50f89a53d00bdeb77cb4758d73d823cf"
            },
            {
                "domain": ".yz.chsi.com.cn",
                "expirationDate": 1774448393,
                "name": "Hm_lvt_3916ecc93c59d4c6e9d954a54f37d84c",
                "path": "/",
                "sameSite": "unspecified",
                "storeId": "0",
                "value": "1740497368,1742707319"
            },
            {
                "domain": ".yz.chsi.com.cn",
                "name": "HMACCOUNT",
                "path": "/",
                "sameSite": "unspecified",
                "storeId": "0",
                "value": "98DE3C943B5DB9F6"
            },
            {
                "domain": "yz.chsi.com.cn",
                "name": "XSRF-CCKTOKEN",
                "path": "/",
                "sameSite": "unspecified",
                "storeId": "0",
                "value": "fcb676f100250f5c5e6ac39febaa59e6"
            },
            {
                "domain": "yz.chsi.com.cn",
                "name": "CHSICC_CLIENTFLAGCHSI",
                "path": "/",
                "sameSite": "unspecified",
                "storeId": "0",
                "value": "43fc98c2043067034d755fa6b965b98d"
            },
            {
                "domain": "yz.chsi.com.cn",
                "name": "CHSICC_CLIENTFLAGZSML",
                "path": "/",
                "sameSite": "unspecified",
                "storeId": "0",
                "value": "ad6cd6f56ff84e20c3c0da9cb563051c"
            },
            {
                "domain": ".chsi.com.cn",
                "expirationDate": 1777268226.926107,
                "name": "_ga_TT7MCH8RRF",
                "path": "/",
                "sameSite": "unspecified",
                "storeId": "0",
                "value": "GS1.1.1742708157.1.1.1742708226.0.0.0"
            },
            {
                "domain": ".chsi.com.cn",
                "expirationDate": 1745300227,
 
                "name": "CHSICLTID",
                "path": "/",
                "sameSite": "unspecified",
 
                "storeId": "0",
                "value": "CA1.1.ebaf1fbded25286ea27cb45e29b217bc"
            },
            {
                "domain": ".chsi.com.cn",
                "expirationDate": 1777268227.242157,
    
                "name": "CHSIDSTID",
                "path": "/",
                "sameSite": "unspecified",
   
                "storeId": "0",
                "value": "195c1802b8efc1-00ec0755d7217c-1b525636-2d9000-195c1802b8f10e6"
            },
            {
                "domain": ".chsi.com.cn",
                "expirationDate": 1742998802,

                "name": "_gid",
                "path": "/",
                "sameSite": "unspecified",

                "storeId": "0",
                "value": "GA1.3.2100649133.1742822753"
            },
            {
                "domain": "yz.chsi.com.cn",
       
                "name": "JSESSIONID",
                "path": "/",
                "sameSite": "unspecified",

                "storeId": "0",
                "value": "CE8D7FBC73F41048C6218889AA752B8A"
            },
            {
                "domain": ".yz.chsi.com.cn",
  
                "name": "Hm_lpvt_3916ecc93c59d4c6e9d954a54f37d84c",
                "path": "/",
                "sameSite": "unspecified",

                "storeId": "0",
                "value": "1742912393"
            },
            {
                "domain": ".chsi.com.cn",
                "expirationDate": 1777472403.033066,
    
                "name": "_ga",
                "path": "/",
                "sameSite": "unspecified",

                "storeId": "0",
                "value": "GA1.1.1526983776.1740497369"
            },
            {
                "domain": ".chsi.com.cn",
                "expirationDate": 177747214.61978,
                "name": "_ga_YZV5950NX3",
                "path": "/",
                "sameSite": "unspecified",
                "storeId": "0",
                "value": "GS1.1.1742911751.7.1.1742912614.0.0.0"
            }
        ]
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=cookies, dont_filter=True)

    def parse(self, response, **kwargs):
        self.logger.info(f"软件工程专业招生计划 {response.text}")



        # 发起详情页请求
        # detail_url = f"https://yz.chsi.com.cn/zsml/querySchAction.do?ssdm=&dwmc={school_name}&yjxkdm=0854"
        # yield scrapy.Request(
        #     detail_url,
        #     callback=self.parse_detail,
        #     meta={'item': item},  # 传递已获取的数据
        #     dont_filter=True  # 允许重复URL
        # )
