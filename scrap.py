# for multiple pages

import requests
from bs4 import BeautifulSoup
import pandas as pd

Product_name  = []
Prices = []
Description = []
Rating = []

for i in range(2,4):
    URL = "https://www.flipkart.com/search?q=headphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    page = requests.get(URL)

    soup = BeautifulSoup(page.text, "lxml")

    box = soup.find('div', class_="_1YokD2 _3Mn1Gg")

    names = box.find_all('a',class_="s1Q9rs")
    prices = box.find_all('div',class_="_30jeq3")
    desriptions = box.find_all('div', class_="_3Djpdu")
    reviews = box.find_all('div',class_="_3LWZlK")

    for name in names:
        P_name = name.text
        Product_name.append(P_name) 
    
    for price in prices:
        Pr_name = price.text
        Prices.append(Pr_name)


    for description in desriptions:
        D_name = description.text
        Description.append(D_name)
    

    for review in reviews:
        R_name = review.text
        Rating.append(R_name)

    print(len(Rating))
    
    

df = pd.DataFrame({"Product_name":Product_name,"Prices":Prices,"Description":Description,"Rating":Rating})
print(df)
    
    
df.to_csv("Headphone_data.csv")

