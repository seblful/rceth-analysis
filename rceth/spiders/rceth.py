from gc import callbacks
from subprocess import call
from urllib.request import Request
import scrapy
from ..items import RcethItem
from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest
from scrapy.shell import inspect_response
import requests

class RcethSpider(scrapy.Spider):
    name = 'rceth'
    start_urls = ['https://rceth.by/Refbank/reestr_lekarstvennih_sredstv/results']

    def parse(self, response):
        dict_token = {'QueryStringFind': 'Rk9wdC5WQW5bPV1GYWxzZVs7XUZPcHQuVlVuVGVybVs9XUZhbHNlWztdRk9wdC5WUGF1c2VbPV1GYWxzZVs7XUZPcHQuVkZpbGVzWz1dVHJ1ZVs7XUZPcHQuVkVGaWVsZDFbPV1UcnVlWztdRk9wdC5PcmRlckJ5Wz1dTl9MUFs7XUZPcHQuRGlyT3JkZXJbPV1hc2NbO11GT3B0LlZUWz1ddFs7XUZPcHQuUGFnZUNbPV0xMDBbO11GT3B0LlBhZ2VOWz1dMls7XUZPcHQuQ1JlY1s9XTU3OTlbO11GT3B0LkNQYWdlWz1dNThbO11GUHJvcHNbMF0uTmFtZVs9XU5fTFBbO11GUHJvcHNbMF0uSXNUZXh0Wz1dVHJ1ZVs7XUZQcm9wc1swXS5Dcml0RWxlbXNbMF0uVmFsWz1dZGFzZGFzZHNbO11GUHJvcHNbMF0uQ3JpdEVsZW1zWzBdLkV4Y2xbPV1UcnVlWztdRlByb3BzWzBdLkNyaXRFbGVtc1swXS5Dcml0Wz1dTGlrZVs7XUZQcm9wc1swXS5Dcml0RWxlbXNbMF0uTnVtWz1dMVs7XUZQcm9wc1sxXS5OYW1lWz1dTl9NUFs7XUZQcm9wc1sxXS5Jc1RleHRbPV1UcnVlWztdRlByb3BzWzFdLkNyaXRFbGVtc1swXS5WYWxbPV1fWztdRlByb3BzWzFdLkNyaXRFbGVtc1swXS5FeGNsWz1dRmFsc2VbO11GUHJvcHNbMV0uQ3JpdEVsZW1zWzBdLkNyaXRbPV1MaWtlWztdRlByb3BzWzFdLkNyaXRFbGVtc1swXS5OdW1bPV0xWztdRlByb3BzWzJdLk5hbWVbPV1UeXBlWztdRlByb3BzWzJdLklzRHJvcFs9XVRydWVbO11GUHJvcHNbMl0uQ3JpdEVsZW1zWzBdLlZhbFs9XV9bO11GUHJvcHNbMl0uQ3JpdEVsZW1zWzBdLkV4Y2xbPV1GYWxzZVs7XUZQcm9wc1syXS5Dcml0RWxlbXNbMF0uQ3JpdFs9XUxpa2VbO11GUHJvcHNbMl0uQ3JpdEVsZW1zWzBdLk51bVs9XTFbO11GUHJvcHNbM10uTmFtZVs9XUFUQ1s7XUZQcm9wc1szXS5Jc1RleHRbPV1UcnVlWztdRlByb3BzWzNdLkNyaXRFbGVtc1swXS5WYWxbPV1fWztdRlByb3BzWzNdLkNyaXRFbGVtc1swXS5FeGNsWz1dRmFsc2VbO11GUHJvcHNbM10uQ3JpdEVsZW1zWzBdLkNyaXRbPV1MaWtlWztdRlByb3BzWzNdLkNyaXRFbGVtc1swXS5OdW1bPV0xWztdRlByb3BzWzRdLk5hbWVbPV1OX0ZSWztdRlByb3BzWzRdLklzVGV4dFs9XVRydWVbO11GUHJvcHNbNF0uQ3JpdEVsZW1zWzBdLlZhbFs9XV9bO11GUHJvcHNbNF0uQ3JpdEVsZW1zWzBdLkV4Y2xbPV1GYWxzZVs7XUZQcm9wc1s0XS5Dcml0RWxlbXNbMF0uQ3JpdFs9XUxpa2VbO11GUHJvcHNbNF0uQ3JpdEVsZW1zWzBdLk51bVs9XTFbO11GUHJvcHNbNV0uTmFtZVs9XU5fRlZbO11GUHJvcHNbNV0uSXNUZXh0Wz1dVHJ1ZVs7XUZQcm9wc1s1XS5Dcml0RWxlbXNbMF0uVmFsWz1dX1s7XUZQcm9wc1s1XS5Dcml0RWxlbXNbMF0uRXhjbFs9XUZhbHNlWztdRlByb3BzWzVdLkNyaXRFbGVtc1swXS5Dcml0Wz1dTGlrZVs7XUZQcm9wc1s1XS5Dcml0RWxlbXNbMF0uTnVtWz1dMVs7XUZQcm9wc1s2XS5OYW1lWz1dQ29tcGFueV9EZWNsYXJhbnRbO11GUHJvcHNbNl0uSXNUZXh0Wz1dVHJ1ZVs7XUZQcm9wc1s2XS5Dcml0RWxlbXNbMF0uVmFsWz1dX1s7XUZQcm9wc1s2XS5Dcml0RWxlbXNbMF0uRXhjbFs9XUZhbHNlWztdRlByb3BzWzZdLkNyaXRFbGVtc1swXS5Dcml0Wz1dTGlrZVs7XUZQcm9wc1s2XS5Dcml0RWxlbXNbMF0uTnVtWz1dMVs7XUZQcm9wc1s3XS5OYW1lWz1dTlJFR1s7XUZQcm9wc1s3XS5Jc1RleHRbPV1UcnVlWztdRlByb3BzWzddLkNyaXRFbGVtc1swXS5WYWxbPV1fWztdRlByb3BzWzddLkNyaXRFbGVtc1swXS5FeGNsWz1dRmFsc2VbO11GUHJvcHNbN10uQ3JpdEVsZW1zWzBdLkNyaXRbPV1MaWtlWztdRlByb3BzWzddLkNyaXRFbGVtc1swXS5OdW1bPV0xWztdRlByb3BzWzhdLk5hbWVbPV1EYXRhWztdRlByb3BzWzhdLklzRGF0ZVs9XVRydWVbO11GUHJvcHNbOF0uQ3JpdEVsZW1zRC5WYWwxWz1dbnVsbFs7XUZQcm9wc1s4XS5Dcml0RWxlbXNELlZhbDJbPV1udWxsWztdRlByb3BzWzhdLkNyaXRFbGVtc0QuQ3JpdFs9XUVxdWFsWztdRlByb3BzWzldLk5hbWVbPV1URVJNWztdRlByb3BzWzldLklzRGF0ZVs9XVRydWVbO11GUHJvcHNbOV0uQ3JpdEVsZW1zRC5WYWwxWz1dbnVsbFs7XUZQcm9wc1s5XS5Dcml0RWxlbXNELlZhbDJbPV1udWxsWztdRlByb3BzWzldLkNyaXRFbGVtc0QuQ3JpdFs9XUVxdWFsWztd',
                      'FProps[0].CritElems[0].Val' : 'asdadasdads',
                      'FProps[0].CritElems[0].Excl' : 'true',
                      'FOpt.VEField1' : 'true',
                      'IsPostBack' : 'true',
                      'PropSubmit' : 'FOpt_PageN',
                      'ValueSubmit' : '1'
                      }

        headers = {'Content-Type' : 'application/x-www-form-urlencoded'}

        yield FormRequest.from_response(response, formdata=dict_token, headers = headers , callback = self.start_scraping)
        while int(dict_token['ValueSubmit']) <= 58:
            dict_token['ValueSubmit'] = str(int(dict_token['ValueSubmit']) + 1)
            yield FormRequest.from_response(response, formdata=dict_token, headers = headers , callback = self.start_scraping)
        

    def start_scraping(self, response):
        for row in response.css("#content > div > div.results > div.table-view > table > tbody > tr"):
            items = RcethItem()
            
            trade_name = row.css("tr>td>a::text").get()
            international_name = row.css("td:nth-child(3)::text").get().rstrip()
            dosage_form = list(map(lambda x: x.replace(';','').rstrip().lstrip(), row.xpath("td[4]/text()").extract()))
            manufacturer = row.css("td:nth-child(5)::text").get().strip()
            applicant = row.css("td:nth-child(6)::text").get().strip()
            number_of_certificate = row.css("td:nth-child(7)::text").get().strip()
            registration_date = row.css("td:nth-child(8)::text").get().strip()
            validity = row.css("td:nth-child(9)::text").get().strip()
            original = row.css("td:nth-child(10)::text").get().strip()
            link_of_instruction = list(map(lambda x: "https://rceth.by/" + x, row.css("tr>td>span>a::attr(href)").extract()))
            
            items['trade_name'] = trade_name
            items['international_name'] = international_name
            items['dosage_form'] = dosage_form
            items['manufacturer'] = manufacturer
            items['applicant'] = applicant
            items['number_of_certificate'] = number_of_certificate
            items['registration_date'] = registration_date
            items['validity'] = validity
            items['original'] = original
            items['link_of_instruction'] = link_of_instruction
            
            inner_url = "https://rceth.by/" + row.css("tr>td>a::attr(href)").get()
            yield response.follow(inner_url, callback=self.parse_product, meta={'items' : items})

            
    def parse_product(self, response):
        items = response.meta['items']

        composition = response.xpath("//tbody/tr[1]/td[2]/text()").get().strip()
        ATC_code = response.xpath("//tr[2]/td[2]/a/text()").get()
        prescribed = response.xpath("//tr[10]/td[2]/text()").get().strip()
        storage_list = response.xpath("//tr[11]/td[2]/text()").get().strip()
        term_of_usage = response.xpath("//tr[12]/td[2]/text()").get().strip()
        
        items['composition'] = composition
        items['ATC_code'] = ATC_code
        items['prescribed'] = prescribed
        items['storage_list'] = storage_list
        items['term_of_usage'] = term_of_usage
        
        yield items