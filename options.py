import requests
import re
from datetime import datetime


ticker = "TSLA"
#ticker = input("Enter the ticket:")



apiUrl = 'https://yfapi.net/v6/finance/quote?region=US&lang=en&symbols=' + ticker
headers =  { 'X-API-KEY':  'ssEgcba1ai1kOmUNiu0Pl8gpD3YGADUx18oFrEBc' }

start1 = datetime.now()
stockRequest = requests.get(apiUrl, headers = headers )
tickerObject = stockRequest.json()
end1 = datetime.now()
duration1 = end1 - start1
payloadSize1 = len(stockRequest.text)
print("Duration1:", duration1, "Size: ", int(payloadSize1 / 1024))

if tickerObject['quoteResponse']['result'] != []:
  print(tickerObject['quoteResponse']['result'][0]['ask'] )
else:
  print("Unable to find the ticker sybmol " + ticker )


start2 = datetime.now()
response = requests.get("https://finance.yahoo.com/quote/" + ticker)
htmlResponseOfYahhoo = response.text 
payloadSize2 = len(response.text)
matches = re.search('Lead-4-QuoteHeader-Proxy.*?data-reactid=\"49\">(.*?)<\/span>',htmlResponseOfYahhoo)
stockPrice = matches.group(1)
end2 = datetime.now()
duration2 = end2 - start2
print("Duration2:", duration2, "Size: ", int(payloadSize2 / 1024) )

print(stockPrice)