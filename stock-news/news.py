import os
import requests
from twilio.rest import Client
from price import StockPrice

# Refer https://newsapi.org/docs/endpoints/everything
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')


class CompanyNews:
    def __init__(self, name, sp: StockPrice):
        self.company_name = name
        self.stock_price = sp
        self.message = None

    def send_news_sms(self):
        news_params = {
            'apiKey': NEWS_API_KEY,
            'qInTitle': self.company_name,
        }

        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()['articles']

        three_articles = articles[:3]

        trend = self.stock_price.stock_trend()
        formatted_articles = [f"{trend}%\nHeadline: {article['title']}\n" \
                              f"Brief:]{article['description']}" for article in three_articles]

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        for article in formatted_articles:
            print(article)
            message = client.messages.create(
                from_='+11234567890',
                body=article,
                to='+10123456789'
            )

            print(message.status)
