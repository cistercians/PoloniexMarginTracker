import os
import csv
import time
import requests

field_names = ['BTC', 'ETH', 'LTC', 'XRP', 'STR', 'XMR', 'DASH', 'BTS', 'MAID', 'FCT', 'DOGE', 'CLAM']
csv_file = open('data.csv', 'w')

writer = csv.DictWriter(csv_file, fieldnames=field_names)
writer.writeheader()

while True:
    
    poloniex = requests.get('https://poloniex.com/public?command=returnTicker').json()
    
    BTC = poloniex["USDT_BTC"]
    ETH = poloniex["BTC_ETH"]
    LTC = poloniex["BTC_LTC"]
    XRP = poloniex["BTC_XRP"]
    STR = poloniex["BTC_STR"]
    XMR = poloniex["BTC_XMR"]
    DASH = poloniex["BTC_DASH"]
    BTS = poloniex["BTC_BTS"]
    MAID = poloniex["BTC_MAID"]
    FCT = poloniex["BTC_FCT"]
    DOGE = poloniex["BTC_DOGE"]
    CLAM = poloniex["BTC_CLAM"]
    
    writer.writerow({'BTC': BTC["percentChange"],
                     'ETH': ETH["percentChange"],
                     'LTC': LTC["percentChange"],
                     'XRP': XRP["percentChange"],
                     'STR': STR["percentChange"],
                     'XMR': XMR["percentChange"],
                     'DASH': DASH["percentChange"],
                     'BTS': BTS["percentChange"],
                     'MAID': MAID["percentChange"],
                     'FCT': FCT["percentChange"],
                     'DOGE': DOGE["percentChange"],
                     'CLAM': CLAM["percentChange"],})
    
    csv_file.flush()
    os.fsync(csv_file.fileno())
    time.sleep(60)

    # this line is optional, you can delete it.
    print('Info appended.')
