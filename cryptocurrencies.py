
from cgi import print_exception
from ctypes.wintypes import FLOAT
from threading import activeCount
from tokenize import Name
from urllib.request import urlopen, Request
from platform import release
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font
from twilio.rest import Client

url = 'https://www.livecoinwatch.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

		
req = Request(url, headers=headers)

webpage= urlopen(req).read()		

soup= BeautifulSoup(webpage, 'html.parser')

title =soup.title   

print(title.text)

table_rows =soup.findAll("tr")

for row in table_rows[1:6]:
    td =row.findAll("td")
    name= td[1].text.strip()
    price=td[2].text.strip()
    percentage_change=td[8].text.strip()
    corresponding_price=float(price.replace(",","").replace("$",""))*float(percentage_change.strip('%'))
   

    print(f"Name:{name}")
    print(f"Cureent Price: {price}")
    print(f"% Change last 24h: {percentage_change}")
    print(f"Corresponding Price:  {corresponding_price}")

    input()

