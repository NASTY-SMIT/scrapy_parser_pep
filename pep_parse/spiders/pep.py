import scrapy
import re

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css(
            'a.pep.reference.internal::attr(href)').getall()
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        info = response.css('h1.page-title::text').get()
        number = re.search(r'PEP\s+(\d+)\s+', info).group(1)
        name = info.split('–')[1].strip()
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': int(number),
            'name': name,
            'status': status}
        yield PepParseItem(data)
