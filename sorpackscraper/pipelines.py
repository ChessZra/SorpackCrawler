# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import json 

class SorpackscraperPipeline:
    def open_spider(self, spider):
        self.file = open('output.json', 'w')
        self.file.write("[\n")
        logging.info("Output file opened.")
        print("Output file opened.")
        self.first_item = True
        
    def close_spider(self, spider):
        self.file.write("\n]")
        self.file.close()
        logging.info("Output file closed.")
        print("Output file closed.")

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        if self.first_item:
            self.file.write(line)
            self.first_item = False
        else:
            self.file.write(",\n" + line)
        logging.info("Item processed: %s", line)
        print("Item processed: %s", line)
        return item

