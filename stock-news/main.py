from price import StockPrice
from news import CompanyNews

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

sp = StockPrice(STOCK_NAME)
company_news = CompanyNews(COMPANY_NAME, sp)
company_news.send_news_sms()
