import pymysql
from graduate_info import settings

class GraduateInfoPipeline:
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DATABASE,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWORD,
            port=settings.MYSQL_PORT,
            charset='utf8mb4'
        )
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS graduate_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            school_name VARCHAR(100),
            major VARCHAR(100),
            department VARCHAR(100),
            score_line TEXT,
            adjust_info TEXT,
            pub_date DATE,
            source_url VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.cursor.execute(sql)
        self.connect.commit()

    def process_item(self, item, spider):
        sql = """
        INSERT INTO graduate_info(
            school_name, major, department, score_line, 
            adjust_info, pub_date, source_url
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(sql, (
            item['school_name'],
            item['major'],
            item['department'],
            item['score_line'],
            item['adjust_info'],
            item['pub_date'],
            item['source_url']
        ))
        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()