import scrapy
import selenium

class   LinkedIn(scrapy.Spider):
    name = "LinkedIn"

    start_urls= [
        "https://www.welcometothejungle.com/fr/jobs?refinementList%5Bcontract_type_names.fr%5D%5B%5D=Stage&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Fullstack&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Backend&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=DevOps%20%2F%20Infra&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Science&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Autres&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Recherche%20%2F%20R%26D&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Analysis&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Engineering&page=1&configure%5Bfilters%5D=website.reference%3Awttj_fr&configure%5BhitsPerPage%5D=30&aroundLatLng=48.8546%2C2.3477&aroundQuery=Paris%2C%20France&aroundRadius=20000&aroundPrecision=20000"
    ]

        
    def parse(self, response):
        for link in response.xpath("//ul[@class='ais-Hits-list']/li/article/a"):
            offer = link.xpath(".//@href").get()
            yield response.follow(offer, callback=self.parse_offer)
        
        next_page = response.xpath("//li[@class='ais-Pagination-item ais-Pagination-item--nextPage']/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_list(self, response):
        for link in response.xpath("//ul[@class='ais-Hits-list']/li/article/a"):
            offer = link.xpath(".//@href").get()
            yield response.follow(offer, callback=self.parse_offer)
        
        next_page = response.xpath("//li[@class='ais-Pagination-item ais-Pagination-item--nextPage']/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_offer(self, response):
        text = response.xpath("//div[@class='sc-11unfkk-2 NggfW']//text()").getall()
        joined_text = ''.join(text).lower()
        offer = response.xpath("//h1[@class='sc-12bzhsi-3 kaJlvc']//text()").get()
        company = response.xpath("//h3[@class='sc-12bzhsi-9 gOYEPp']//text()").get()
        if self.language.lower() in joined_text:
            yield {
               offer + " chez " + company + " (" + self.language + ")": response.request.url,
            }