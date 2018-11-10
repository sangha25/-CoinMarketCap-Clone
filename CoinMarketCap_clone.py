import requests
from prettytable import PrettyTable
listings_api = 'https://api.coinmarketcap.com/v2/listings/'
ticker_api = 'https://api.coinmarketcap.com/v2/ticker/?start='
listings_data = requests.get(listings_api).json()['data']

table = PrettyTable()
table.field_names = ['Name','Symbol','Price','Volume','MarketCap','Change 1h','Change 24h','Change 7d']
