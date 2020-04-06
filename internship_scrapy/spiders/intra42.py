import scrapy
from internship_scrapy.items import InternshipScrapyItem

class   Intra42(scrapy.Spider):
    name = "Intra42"

    start_urls= [
        "https://companies.intra.42.fr/en/offers"
    ]

    def parse(self, response):
        for link in response.xpath("//div[@class='page-content']/div/h3/a"):
            offer = link.xpath(".//@href").get()
            print("\n\n\n" + offer + "\n\n\n")
            yield response.follow(offer, callback=self.parse_offer)

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_offer(self, response):
        text = response.xpath("//div[@class='show-offer']//text()").getall()
        joined_text = ''.join(text).lower()
        language = getattr(self, 'language', None)
        if language.lower() in joined_text:
            item = InternshipScrapyItem()
            company = response.xpath("//div[@class='show-offer']/(div[@class='flex-item'])[2]/div[@class='show-right']/div[@class='title']/a//text()").get()
            offer = response.xpath("//div[@class='show-left company-name']/h2//text()").get()
            item['title'] = offer + " chez " + company + " (" + language + ")"
            item['url'] = response.request.url
            yield item