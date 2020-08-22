import scrapy
from scrapingnews.items import NewsItem
from scrapy.loader import ItemLoader

class NewsSpider(scrapy.Spider):
	name= 'news'

	start_urls=[
		'https://www.bbc.com/indonesia'
	]

	def parse(self, response):
		for feature in response.xpath("//section[@aria-labelledby='Features']/ul/li"):
			l = ItemLoader(item= NewsItem(),selector=feature)
			l.add_xpath('news_title', ".//div/div/h3/a")
			yield l.load_item()
			

		next_page= response.xpath("//section[@aria-labelledby='Features']//div/h2/a/@href").extract_first()
		if next_page is not None:
			next_page_link = response.urljoin(next_page)
			#A request represents an HTTP request generated in the spider and executed by the downloader, generating a response
			#Callback is a function that will be called if the request is downloaded
			yield scrapy.Request(url= next_page_link, callback=self.parse)