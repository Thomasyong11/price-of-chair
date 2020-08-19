__author__ = 'yong'

import requests
from bs4 import BeautifulSoup
request = requests.get("https://www.johnlewis.com/john-lewis-partners-abraham-office-chair/tan/p3361768")
content = request.content #(content of the page)
soup = BeautifulSoup(content, "html.parser")



element = soup.find("p", {"class": "price price--large"})

string_price = element.text.strip()
price_without_symbol = string_price[1:] #copy elements from string price to price without string from the second place thus removing the symbol
price = float(price_without_symbol) #price as a float to compare
if price<500:
    print("You should buy the item")
    print("The price is {}".format(string_price))
else:
    print("Do not buy, it's expensive")
#print(element.text.strip())
# requseting the info of johnlewis.com
# using soup as a variable telling us to use beautifulsoup function to search through the content using html parser
# finding the price
# <p class="price price--large">£299.00</p> (what i used for line 11)
# printing the details from the webpage as text using strip to reorganise the text