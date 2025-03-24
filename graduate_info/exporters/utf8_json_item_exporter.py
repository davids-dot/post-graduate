from scrapy.exporters import JsonLinesItemExporter
from scrapy.exporters import JsonItemExporter


class Utf8JsonLinesItemExporter(JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        kwargs['ensure_ascii'] = False
        kwargs['encoding'] = 'utf-8'
        super(Utf8JsonLinesItemExporter, self).__init__(file, **kwargs)

# class Utf8JsonItemExporter(JsonItemExporter):
#     def __init__(self, file, **kwargs):
#         super(Utf8JsonItemExporter, self).__init__(
#             file, ensure_ascii=False, **kwargs)