# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst
from w3lib.html import remove_tags


class NewsItem(scrapy.Item):
   	
    news_title = scrapy.Field(
    	input_processor = MapCompose(remove_tags),
    	output_processor = TakeFirst()
    )
    
