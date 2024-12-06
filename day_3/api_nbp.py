from typing import List

import requests
from pydantic import BaseModel

url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

response = requests.get(url)
print(response)
# <Response [200]> ok
# 3xx - warning, redirect
# 4xx - 404 - brak strony, 400 Bad Request - błąd w parametrach
# 5xx - blędy po stronie serwera
print(response.text)
# {"table": "A", "currency": "dolar amerykański", "code": "USD",
#  "rates": [{"no": "237/A/NBP/2024", "effectiveDate": "2024-12-06", "mid": 4.0341}]}
data = response.json()
print(type(data))  # <class 'dict'>
print(data)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '237/A/NBP/2024', 'effectiveDate': '2024-12-06', 'mid': 4.0341}]}
print(data['rates'])  # [{'no': '237/A/NBP/2024', 'effectiveDate': '2024-12-06', 'mid': 4.0341}]
print(data['rates'][0]['mid'])  # 4.0341


class Rates(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class Currency(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rates]


currency = Currency(**response.json())
print(currency)
print(type(currency))
# table = 'A'
# currency = 'dolar amerykański'
# code = 'USD'
# rates = [Rates(no='237/A/NBP/2024', effectiveDate='2024-12-06', mid=4.0341)]
# <
#
# class '__main__.Currency'>
print(currency.rates[0].mid)  # 4.0341
