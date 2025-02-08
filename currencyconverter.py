import requests


API_KEY = 'fca_live_mtW2Qz8bFmihFrf02VsugauY2TSOQpYPVmzAun46'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
CURRENCIES = ["USD","CAD","EUR","AUD","CNY","INR"]


def converts_currency(base):
  currencies = ",".join(CURRENCIES)
  url = f"{BASE_URL}& base_currency={base}&currencies={currencies}"

  try:
    
    response = requests.get(url)
    data = response.json()
 
    return data["data"]
  except:
    print('invalid currency')
    return None
  
while True:
 base = input("(1):USD (2):INR (3):CAD (4):EUR (5):AUD (6):CNY")  
 if base == '1':
    base = "USD"
 elif base == '2':
   base="INR"
 elif base == '3':
   base = "CAD"
 elif base == '4':
   base =    "EUR"
 elif base == '5':
   base = "AUD"
 elif base == '6':
   base = "CNY"
 else:
   print('invalid input')

 data = converts_currency(base)
 if base == 'q':
    break
 else:

   for ticker ,value in data.items():
    print(f'{ticker}:{value}')