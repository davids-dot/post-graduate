import scrapy
from graduate_info.items import ShcoolItem
from datetime import datetime

class SchoolCrawlerSpider(scrapy.Spider):
    name = "school_crawler"
    allowed_domains = ["yz.chsi.com.cn"]
    start_urls = ["https://yz.chsi.com.cn/sch/"]

    def parse(self, response):
        for school in response.css('.sch-list-container > .sch-item'):
            item = ShcoolItem()
            
            # 直接使用 get(default='').strip() 避免 None 值，并去除空白
            item['school_name'] = school.css('.name::text').get(default='').strip()
            item['logo_url'] = school.css('img::attr(src)').get(default='').strip()
            
            # 处理双引号问题
            tag = school.css('.sch-tag::text').get(default='').strip()
            item['tag'] = tag if tag else None
            
            # 将自划线转换为布尔值
            self_eval = '自划线' in ''.join(school.css('.sch-department::text').getall())
            item['self_evaluation'] = self_eval
            
            # 处理链接
            links = school.css('.sch-link a')
            for link in links:
                text = link.css('::text').get(default='').strip()
                url = response.urljoin(link.css('::attr(href)').get(default='').strip())
                
                if '网报公告' in text:
                    item['notice'] = url
                elif '招生简章' in text:
                    item['enrollment_guide'] = url
                elif '在线咨询' in text:
                    item['online_consult_url'] = url
                elif '调剂办法' in text:
                    item['adjustment_method'] = url
            
            yield item

        # 获取下一页链接
        next_page = response.css('.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)