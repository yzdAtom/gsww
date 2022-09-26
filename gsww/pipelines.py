# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class GswwPipeline:
    def open_spider(self, spider):
        self.fp = open("gushiwen.txt", "w", encoding="utf-8")

    def process_item(self, item, spider):
        # print("*"*30)
        # print(item)
        # print("*"*30)
        self.fp.write(json.dumps(dict(item), ensure_ascii=False) + "\n")
        # 需要返回item，因为item可能需要给下一个pipeline处理
        return item

    def close_spider(self,spider):
        self.fp.close()
