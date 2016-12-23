import scrapy
from jadwal_solat.items import JadwalSolatItem

class Jadwal_solat(scrapy.Spider):
    name = "jadwal_solat"
    # page = 1
 
    def start_requests(self):
        url = 'http://jadwalsholat.pkpu.or.id/'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        pages = response.xpath("//select[@class='inputcity']//option/@value").extract()
        requests =[scrapy.Request("http://jadwalsholat.pkpu.or.id/monthly.php?id="+str(page), self.parse_data) for page in pages]
        return requests
        
    def parse_data(self, response):
        idKota = response.xpath('//select[@class="inputcity"]//option[@selected="selected"]/@value').extract_first()
        namaKota = response.xpath('//select[@class="inputcity"]//option[@selected="selected"]/text()').extract_first()
        
        tr_light = response.xpath("//tr[@class='table_light']")
        tr_dark = response.xpath("//tr[@class='table_dark']")
        tr_highlight = response.xpath("//tr[@class='table_highlight']")
        tr = tr_light + tr_dark + tr_highlight
              
        data = []
        for td in tr:
            item = JadwalSolatItem()
            item['idKota'] = idKota
            item['namaKota'] = namaKota
            item['hari'] = td.xpath("td//b/text()").extract_first() 
            item['shubuh'] = td.xpath("td/text()").extract()[0]
            item['terbit'] = td.xpath("td/text()").extract()[1]
            item['dzuhur'] = td.xpath("td/text()").extract()[2]
            item['ashar'] = td.xpath("td/text()").extract()[3]
            item['magrib'] = td.xpath("td/text()").extract()[4]
            item['isya'] = td.xpath("td/text()").extract()[5]
            data.append(item)
        return data
