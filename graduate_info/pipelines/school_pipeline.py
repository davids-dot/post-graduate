import mysql.connector
from graduate_info import settings

class SchoolPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=settings.MYSQL_HOST,
            database=settings.MYSQL_DATABASE,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASSWORD,
            port=settings.MYSQL_PORT
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = """
        INSERT IGNORE INTO school (
            school_name, logo_url, tag, self_evaluation, 
            notice, enrollment_guide, online_consult_url, adjustment_method
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            item['school_name'],
            item['logo_url'],
            item['tag'],
            item['self_evaluation'],
            item['notice'],
            item['enrollment_guide'],
            item['online_consult_url'],
            item['adjustment_method']
        )
        self.cursor.execute(sql, values)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()