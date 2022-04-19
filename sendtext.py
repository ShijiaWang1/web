from cgitb import text
import requests
from urllib.request import urlopen, Request
from platform import release
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font
from twilio.rest import Client

url = 'https://www.livecoinwatch.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

		
def get_price(url,headers):

    req = Request(url, headers=headers)

    webpage= urlopen(req).read()		

    soup= BeautifulSoup(webpage, 'html.parser')  

    table_rows =soup.findAll("tr")

    for row in table_rows[1:2]:
        td =row.findAll("td")
        price = td[2].text.strip()
        convertprice=float(price.replace(",","").replace("$",""))

        print(f"BTC price:{convertprice}")

        if(convertprice<40000):
            sendtext1()
        else:
            print('There is no need to send out message for bitcoin')
    for row in table_rows[2:3]:
        td =row.findAll("td")
        price = td[2].text.strip()
        convertprice=float(price.replace(",","").replace("$",""))

        print(f"ETH price:{convertprice}")
        if(convertprice<3000):
            sendtext2()
        else:
            print('There is no need to send out message for ETH')

def sendtext1():
    accountSID= 'AC22f78ff6511e02ac0c5cc2336829358a'

    authToken= '1d36986101ef9d6329b3a678e9a6a062'

    client= Client(accountSID,authToken)

    Twilionumber= '+18645286038'

    mycellphone= '+12819283513'

    textmessage = client.messages.create(to=mycellphone,
                                    from_=Twilionumber,
                                    body= 'The current bitcoin price is lower than 40000 now go check it out.')
    print(textmessage.status)


def sendtext2():
    accountSID= 'AC22f78ff6511e02ac0c5cc2336829358a'

    authToken= '1d36986101ef9d6329b3a678e9a6a062'

    client= Client(accountSID,authToken)

    Twilionumber= '+18645286038'

    mycellphone= '+12819283513'

    textmessage = client.messages.create(to=mycellphone,
                                    from_=Twilionumber,
                                    body= 'The current ETH price is lower than 3000 now go check it out.')
    print(textmessage.status)

get_price(url, headers)