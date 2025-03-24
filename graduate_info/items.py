import scrapy

class ShcoolItem(scrapy.Item):
    school_name = scrapy.Field()  # 学校名称
    logo_url = scrapy.Field()     # logo_url
    tag = scrapy.Field()          # 学校标签
    self_evaluation = scrapy.Field()    # 自划线
    notice = scrapy.Field()       # 网报公告
    enrollment_guide = scrapy.Field()    # 招生简章
    online_consult_url = scrapy.Field()  # 在线咨询地址
    adjustment_method = scrapy.Field()   # 调剂办法
