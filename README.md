# 研究生调剂信息爬虫

## 项目说明
爬取研究生调剂信息的 Scrapy 爬虫项目。

## 运行命令

### 启动爬虫
```bash
# 仅爬取数据到数据库
scrapy runspider graduate_info/spiders/school_crawler.py

# 同时保存为 JSON 文件
scrapy runspider graduate_info/spiders/school_crawler.py -o school.jsonl
```