import scrapy


class SampleSpider(scrapy.Spider):
    name = "custom_elements"

    def start_requests(self):
        url = 'https://only.digital/en'
        tag = getattr(self, "tag", None)
        if tag is not None:
            url = url + "tag/" + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        test1 = response.xpath("//footer//p/text()")[0].get()
        test2 = response.xpath("//footer//p/text()")[1].get()
        test3 = response.xpath("//footer//p/text()")[2].get()
        
        if test1 == 'Start a project':
            print('test1 passed')
        else:
            print('test1 not passed, ', test1)
        
        if test2 == '+7 (495) 740 99 79':
            print('test2 passed')
        else:
            print('test2 not passed, ', test2)
        
        if test3 == 'hello@only.com.ru':
            print('test3 passed')
        else:
            print('test3 not passed, ', test3)

        
        

        # for quote in response.css("div.quote"):
        #     yield {
        #         "text": quote.css("span.text::text").get(),
        #         "author": quote.css("small.author::text").get(),
        #     }

        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
