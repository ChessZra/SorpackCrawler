import json

import scrapydo
from rich import print
from scrapy.utils.reactor import install_reactor
from twisted.internet import asyncioreactor

from jsonData import Data
from sorpackscraper.spiders.MySpider import MySpider

if __name__ == "__main__":
    # Set up the AsyncioSelectorReactor
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")

    # Set up scrapydo
    print("Initiated scrapydo.setup()")
    scrapydo.setup()
    print("Terminated scrapydo.setup()")

    # Run the spider
    print("Initiating scrapydo.run_spider(MySpider, output_file='output.json')")
    scrapydo.run_spider(MySpider, output_file='output.json')

    # now read the produced json file 
    Data.algorithm()
    print()
    print("[bold underline]developed by VIP-icurzedpumuzup :)[/bold underline]")
    input("Press ENTER to exit.")