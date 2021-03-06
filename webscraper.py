#!/usr/bin/env python3

__author__ = "Adam Karl"

import requests,  datetime, time, keyring
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from twilio.rest import Client

"""
Every 90 seconds, check the top dogecoin wallet for new transactions.
If the last 5 transactions have more output than input, text my phone and exit.
"""

def main():
    check_num = 0
    while(True):
        print("check", check_num)
        check_num += 1

        # stress_test_wallet = 'https://bitinfocharts.com/dogecoin/address/DG2mPCnCPXzbwiqKpE1husv3FA9s5t1WMt'
        big_wallet = 'https://bitinfocharts.com/dogecoin/address/DH5yaieqoZN36fDVciNyRueRGvGLR3mr7L'

        req = Request(big_wallet, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req)

        # grab amounts of all transactions on page
        content = BeautifulSoup(webpage, "html.parser")
        amount_strings = content.find_all('td', attrs={"class": "text-success"})

        total = 0.0;
        for i in range(5):
            amt_str = amount_strings[i].text

            sign = amt_str[0]
            text_start = amt_str[1:].find(' DOGE')
            amt = float(amt_str[1:text_start])
            if sign == '+':
                total += amt
            elif sign == '-':
                total -= amt
            else:
                print("unfound sign:", sign)
                exit()

        if total < 0: # more output than input over last 5 transactions
            #twilio id, not confidential
            account_sid = "ACdaa60d580e7f089ec6d04fc5583071ad"

            #use keyring for private authentication and phone number
            auth_token = keyring.get_password("twilio", account_sid)
            my_number = keyring.get_password("phone", account_sid)

            client = Client(account_sid, auth_token)
            message = client.messages.create(
                to=my_number,
                from_="+19563202956",
                body="CHECK WALLET POP")

            print("CHECK WALLET POP")
            exit()

        time.sleep(90)


if __name__ == "__main__":
    main()
