# The website http://api.nbp.pl contains data on exchange rates published by the National Bank of Poland. The service provides data in json or xml formats. Display the last ten Euro exchange rates in json format in the browser window. Save the data to the euro.json file. Then write a program that displays the data from the euro.json file in the following format:

# Date          Buying Rate     Selling Rate
# ============================================
# 2019-10-25    3.8150          3.9820
# ...           ...             ...

import requests
import json

try:
    print("Getting exchange rates...")
    exchange_rates_data = requests.get('https://api.nbp.pl/api/exchangerates/rates/C/EUR/last/10/?format=json')
except Exception as e:
    print("Something went wrong while trying to get exchange rates.")
    raise e
else:
    print("Exchange rates have been downloaded successfully.")

exchange_rates = json.loads(exchange_rates_data.content)

print("\nLast Euro (EUR) <-> Polish Zloty (PLN) echange rates:\n\nDate\t\tBuying Rate\tSelling Rate\n============================================")

for record in reversed(exchange_rates['rates']):
    print(f"{record['effectiveDate']}\t{record['bid']}\t\t{record['ask']}")
