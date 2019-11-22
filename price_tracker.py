# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:29:06 2019

@author: shubham
"""
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

url = "https://www.amazon.in/Reebok-Runner-Running-Shoes-6-DV8424/dp/B07TRJF9T4/ref=sr_1_28?dchild=1&keywords=reebok+shoes&qid=1571763786&smid=AT95IG9ONZD7S&sr=8-28"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

def check_price(url,headers):
    page = requests.get(url , headers= headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text() 
    print(title.strip())
    
    try:
        price = soup.find(id="priceblock_ourprice").get_text()
        print(price.strip())
    except AttributeError:
        print("price = _")

    try:
        price = soup.find(id="priceblock_dealprice").get_text()
        print(price.strip())
    except AttributeError:
        print("price = _")

    conv_price1 = price

    price = list(price)
    price[3] = '.'
    
    conv_price = float("".join(price[2:7]))
    print(conv_price)

    if(conv_price < 3.899):
        sendsms(url, str(conv_price1))
        print('HEY,MESSAGE HAS BEEN SENT!')
        
def sendsms(url,conv_price1):
    client = Client('AC05649b9ed3ed42bbf4962a51c08df923', '073aef34c5d4d174182745551d40831b')
   # client.messages.create(to = '+918210467848', from_ = '+12098854949', body = 'Hurry up,to purchase your selected item at a reduced amount, the link is given below: '+url)
    client.messages.create(to = '+918210467848', from_ = '+12098854949', body = 'Hurry up,to purchase your selected item at a reduced amount, '+conv_price1+' the link is given below: '+url)


check_price(url, headers)


