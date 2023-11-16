import requests
import os

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = os.environ.get('STOCK_API_KEY')
STOCK_NAME = 'TSLA'


class StockPrice:
    def __init__(self, name):
        self.stock_name = name
        print(self.stock_name)
        self.up_down = None

    def stock_trend(self):

        parameters = {
            'symbol': self.stock_name,
            'apikey': STOCK_API_KEY,
            'function': 'TIME_SERIES_DAILY'
        }
        response = requests.get(STOCK_ENDPOINT, params=parameters)
        response.raise_for_status()
        data = response.json()['Time Series (Daily)']

        data_list = [value for (key, value) in data.items()]

        yesterday_closing_price = data_list[0]['4. close']
        print(yesterday_closing_price)

        day_before_yesterday_closing_price = data_list[1]['4. close']
        print(day_before_yesterday_closing_price)

        diff = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
        if diff > 0:
            self.up_down = '🔺'
        else:
            self.up_down = '🔻'

        diff_percent = round((diff / float(yesterday_closing_price)) * 100)
        print(diff_percent)

        if abs(diff_percent) >= 1:
            return f'{STOCK_NAME}:{self.up_down}{abs(diff_percent)}'
