from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen

req = Request('https://bitinfocharts.com/dogecoin/address/DG2mPCnCPXzbwiqKpE1husv3FA9s5t1WMt', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req)


# print(req.status_code)
content = BeautifulSoup(webpage, "html.parser")

for c in content.find_all('td', attrs={"class": "text-error"}):
    print(c.text)


#//*[@id="table_maina"]/tbody/tr[1]/td[3]/text()
