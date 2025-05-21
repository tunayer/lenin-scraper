import scrapy


class PcrawlerSpider(scrapy.Spider):
    name = "pcrawler"
    allowed_domains = ["marxists.org"]
    start_urls = ["https://www.marxists.org/archive/lenin/works/cw/index.htm"]

    targetWords = ["turkey", "pasha", "ottoman", "mustafa", "kemal", "ismet", "suphi", "ethem", "istanbul", "ankara"]

    def parse(self, response, **kwargs):
        volume_links = response.css("table td a::attr(href)").getall()

        for link in volume_links:
            if link.startswith("volume15") and link.endswith(".htm"):
                full_url = response.urljoin(link)
                yield scrapy.Request(full_url, callback=self.parse_volume)

    def parse_volume(self, response):
        part_links = response.css("table td a::attr(href)").getall()

        for link in part_links:
            if link.endswith(".htm") and not link.startswith("volume"):
                full_url = response.urljoin(link)
                yield scrapy.Request(full_url, callback=self.parse_part)

    def parse_part(self, response):
        paragraphs = response.css("p::text").getall()

        for p in paragraphs:
            for word in self.targetWords:
                if word.lower() in p.lower():
                    yield {
                        "url": response.url,
                        "word": word,
                        "paragraph": p.strip()
                    }
                    break
