import scrapy
from scrapy.crawler import CrawlerProcess
import json
import csv

class Olx(scrapy.Spider):
    name = 'olx'
    url = 'https://www.olx.in/api/relevance/feed?lang=en&location=1000001&showAllCars=true&user=1736c7166d4x302ce817'

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }

    def __init__(self):
        with open('result.csv','w') as csv_file:
            csv_file.write('title, description,location,features,date,price\n')

    def start_requests(self):
        for page in range(0,5):
            yield scrapy.Request(url=self.url + '&page=' + str(page), headers=self.headers, callback=self.parse)

    def parse(self,res):
        data = res.text
        data = json.loads(data)
        
        for offer in data['data']:
            items = {
                'title':offer['title'],
                'description':offer['description'].replace('\n',' '),
                'location': offer['locations_resolved']['COUNTRY_name']+ ', ' +
                            offer['locations_resolved']['ADMIN_LEVEL_1_name']+ ', ' +
                            offer['locations_resolved']['ADMIN_LEVEL_3_name'],
                'features': offer['main_info'],
                'date': offer['display_date'],
                'price': offer['price']['value']['display']
            }

            with open('result.csv', 'a') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=items.keys())
                writer.writerow(items)

# Run Scraper
process = CrawlerProcess()
process.crawl(Olx)
process.start()

# Debug
# Olx.parse(Olx,'')