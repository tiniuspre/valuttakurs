import urllib3
import json

http = urllib3.PoolManager()

r = http.request('GET', 'https://api.coinbase.com/v2/exchange-rates?currency=NOK')

print(r.status)

print((json.loads(r.data.decode('utf8'))))