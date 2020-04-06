import scrapy
from internship_scrapy.items import InternshipScrapyItem

class   JobTeaser(scrapy.Spider):
    name = "JobTeaser"

    start_urls= [
        "https://www.jobteaser.com/fr/job-offers?contract=internship&position_category_uuid=ddc0460c-ce0b-4d98-bc5d-d8829ff9cf11&location=France%3A%3A%C3%8Ele-de-France%3A%3AParis%3A%3AParis..Paris%20(France)&contract_duration=6&locale=fr"
    ]

    def parse(self, response):
        print(response.xpath("//html//text()").getall())
        for link in response.xpath("//div[@class='jds-Layout__column__94LEL']/section/div/div/a"):
            print("\n\n\nHELLO\n\n\n")
            offer = link.xpath(".//@href").get()
            yield response.follow(offer, callback=self.parse_offer)
        
        next_page = response.xpath("//a[@data-icon='chevronRight|alone']/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_offer(self, response):
        text = response.xpath("//div[@class='jt-Text jt-Text--wysiwyg']//text()").getall()
        joined_text = ''.join(text).lower()
        language = getattr(self, 'language', None)
        if language.lower() in joined_text:
            item = InternshipScrapyItem()
            company = response.xpath("//a[@class='jt-Link jt-Link--inverseStyle']//text()").get()
            offer = response.xpath("//h1[@class='jt-Title jt-Title--large jt-Title--resetMargin']//text()").get()
            item['title'] = offer + " chez " + company + " (" + language + ")"
            item['url'] = response.request.url
            yield item