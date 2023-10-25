import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        all_peps = response.css(
            'a.pep.reference.internal::attr(href)').getall()
        for pep_link in all_peps:
            pep_link += '/'
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
