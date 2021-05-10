from bs4 import BeautifulSoup
import requests
import datetime
import time
from urllib.request import Request, urlopen


while(True):
    print("checking.....")

    req = Request('https://bitinfocharts.com/dogecoin/address/DG2mPCnCPXzbwiqKpE1husv3FA9s5t1WMt', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)


    # print(req.status_code)
    content = BeautifulSoup(webpage, "html.parser")

    # finds amounts transfered
    # for c in content.find_all('td', attrs={"class": "text-error"}):
    #     print(c.text)

    times = content.find_all('td', attrs={"class": "utc hidden-phone"})
    latest = times[0].text[:-4]
    fifth = times[5].text[:-4]

    l = datetime.datetime.strptime(latest, '%Y-%m-%d %H:%M:%S')
    f = datetime.datetime.strptime(fifth, '%Y-%m-%d %H:%M:%S')
    difference = (l-f).total_seconds()

    if difference/60 < 5:
        # 5+ transactions in 5 mins
        print("CHECK WALLET POP")
        exit()

    time.sleep(90)
