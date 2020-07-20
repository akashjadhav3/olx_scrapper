import scrapy
from scrapy.crawler import CrawlerProcess

class Olx(scrapy.Spider):
    name = 'olx'
    url = 'https://www.olx.in/api/relevance/feed?lang=en&location=1000001&showAllCars=true&user=1736c7166d4x302ce817'

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }

    def start_requests(self):
        yield scrapy.Request(url=self.url + '&page=0', headers=self.headers, callback=self.parse)

    def parse(self,res):
        print(res.text)

# Run Scraper

process = CrawlerProcess()
process.crawl(Olx)
process.start()