# ... 其他设置保持不变 ...
import os
from dotenv import load_dotenv

load_dotenv()

FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_INDENT = 0
FEED_EXPORT_ENSURE_ASCII = False
FEED_EXPORTERS = {
    'jsonlines': 'graduate_info.exporters.utf8_json_item_exporter.Utf8JsonLinesItemExporter',
}

# MySQL 配置
MYSQL_HOST = 'elasticsearch.cloud.com'
MYSQL_DATABASE = 'love_chat'
MYSQL_USER = 'root'
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_PORT = 3306

# 爬虫设置
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2
COOKIES_ENABLED = True

# 代理设置
# DOWNLOADER_MIDDLEWARES = {
#     'graduate_info.middlewares.proxy_middleware.ProxyMiddleware': 350,
# }

ITEM_PIPELINES = {
    'graduate_info.pipelines.school_pipeline.SchoolPipeline': 300,
}
