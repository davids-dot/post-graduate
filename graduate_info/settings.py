# ... 其他设置保持不变 ...

FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_INDENT = 0
FEED_EXPORT_ENSURE_ASCII = False
FEED_EXPORTERS = {
    'jsonlines': 'graduate_info.exporters.utf8_json_item_exporter.Utf8JsonLinesItemExporter',
}

# MySQL 配置
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'graduate_info'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password'
MYSQL_PORT = 3306

# 爬虫设置
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2
COOKIES_ENABLED = True

# ITEM_PIPELINES = {
#    'graduate_info.pipelines.GraduateInfoPipeline': 300,
# }