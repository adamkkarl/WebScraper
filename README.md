# WebScraper
messing around learning how to build a web scraper for general use


Install Virtual Environment (Windows command line):
$ python3 -m venv env
$ env\Scripts\activate.bat


Inside Virtual Environment
$ pip install bs4  <!--- beautiful soup --->
$ pip install requests <!--- requests --->

Setup keyring
$ pip install keyring
in python
keyring.set_password("twilio", "ACdaa60d580e7f089ec6d04fc5583071ad", "INSERT AUTH TOKEN")
keyring.set_password("phone", "ACdaa60d580e7f089ec6d04fc5583071ad", "INSERT PHONE NUMBER")
