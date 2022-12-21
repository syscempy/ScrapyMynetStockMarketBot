import scrapy


class CrawlingSpider(scrapy.Spider):
    name = 'borsa'
    start_urls = ['https://finans.mynet.com/borsa/hisseler/']

    def parse(self, response):
        # Iterate over the rows in the table
        for row in response.css('table tr'):
            # Extract the data from the row using CSS selectors
            name = row.css('td:nth-child(1) a::text').extract_first()
            first_trading_date = row.css('td:nth-child(2)::text').extract_first()
            last_trading_price = row.css('td:nth-child(3)::text').extract_first()
            buying_price = row.css('td:nth-child(4)::text').extract_first()
            selling_price = row.css('td:nth-child(5)::text').extract_first()
            daily_change = row.css('td:nth-child(6)::text').extract_first()

            # Yield a dictionary with the extracted data
            yield {
                'name': name,
                'first_trading_date': first_trading_date,
                'last_trading_price': last_trading_price,
                'buying_price': buying_price,
                'selling_price': selling_price,
                'daily_change': daily_change,
            }
