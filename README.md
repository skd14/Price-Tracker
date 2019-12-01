                                                    
                                                 *** Price-Trackers ***

**A python script to track the price of the product you were looking to buy for a cheaper rate.
What I used**

    I used BeautifulSoup to parse the html file of the link provided.
    I used Python to check if the product's price is fallen to the desired price.
    I used Twilio Web API to send sms to my mobile phone containing the link if the price has fallen.

**Code Breakdown**
*The Price Checking part*

  -  We have to import requests, BeautifulSoup from bs4.
  - url variable contains the URL of the product you want to track.
  -  headers variable contains My User Agent details (You can get that by typing My User Agent in Google Search Bar)
  - check_price(url, headers) is the function where the magic happens.
      -  page = requests.get(url , headers= headers) this variable page gets the page details containing the whole html document.
      -  soup = BeautifulSoup(page.content, 'html.parser') this variable soup parses that is it takes out each elements and tags.
      -  title = soup.find(id="productTitle").get_text() here title gets you the title of the product in the website.
      -  price = soup.find(id="priceblock_ourprice").get_text() gets you the price of the product, it is inside a try block since during some offer days the id changes to priceblock_dealprice, so accordingly I take the price.
      -  price = list(price) price[3] = '.' this code changes the ',' in price to '.'.
      -  conv_price = float("".join(price[2:7])) this code changes the price from string to float. and hence can be used in the if loop.

         

**Sending SMS**

    For this you need to have a Twilio account which will give you the account id and a phone number so you can send SMS.
    We need to import Client from twilio.rest
    client = Client('','') You have to enter the Account ID and AUTH Token as provided by twilio.
    client.messages.create(to = '', from_='', body='') in to enter the phone number you have to send the message, in from_ enter the phone number provided to you by Twilio, in body enter the message you want to send.
