import os
import csv
import time
import requests

field_names = ['time', 'last', 'vwap', 'high', 'low', 'open', 'vol']
csv_file = open('data.csv', 'w')

writer = csv.DictWriter(csv_file, fieldnames=field_names)
writer.writeheader()

while True:
    info = requests.get('https://www.bitstamp.net/api/ticker/').json()
    writer.writerow({'time': info['timestamp'],
                     'last': info['last'],
                     'vwap': info['vwap'],
                     'high': info['high'],
                     'low': info['low'],
                     'open': info['open'],
                     'vol': info['volume']})
    csv_file.flush()
    os.fsync(csv_file.fileno())
    time.sleep(60)

    # this line is optional, you can delete it.
    print('Info appended.')
