import scrapy
import json
from itemadapter import ItemAdapter
import logging


# to run the code
# scrapy runspider sorpackscraper\spiders\MySpider.py
class MySpider(scrapy.Spider):
    name = 'sorpack'
    start_urls = ['http://sorpack.com/new_plus/shop/shop_card.asp']
    custom_settings = {
        'ITEM_PIPELINES': {
            "sorpackscraper.pipelines.SorpackscraperPipeline": 300
        }
    }
    def balanceToNumberAlgorithm(self, balance):
        price = 0
        if '亿' in balance:
            price += (float(balance[0: balance.find('亿')]) * 100000000) + (float(balance[balance.find('亿') + 1: -1]) * 10000)
        else:
            price += float(balance[0: -1]) * 10000
        return price

    def parse(self, response):
        print('Fetching data...')
        products = response.css('tr[onmouseout]')
        for product in products:
            css_string = product.get()
            data = {
                'serial number': css_string[css_string.find(""";"><td>""") + 7: css_string.find("""</td><td><font""")],
                'card number': css_string[css_string.find("""***</font><""") - 7: css_string.find("""***</font><""") + 3],
                'balance ($)': self.balanceToNumberAlgorithm(css_string[css_string.find("""a84f">""") + 6: css_string.find("""</font></td><td><font color="#ff0000">""")]),
                'price (yuan)': css_string[css_string.find("万") + 39: css_string.find("万") + 43].replace('<','').replace('/','').replace('f','')
            } 
            print(data)
            yield data

        pages = response.css('option[value]').getall()
        for index, page in enumerate(pages):
            if 'selected' in page and index != len(pages) - 1:
                print(f'PAGE {index + 2}. ', end='')
                yield scrapy.Request(f'http://sorpack.com/new_plus/shop/shop_card.asp?p={index + 2}', callback=self.parse)

