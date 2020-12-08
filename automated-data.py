#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import numpy as np

today = date.today()
new_data= {}

#Initial portfolio weights: ORDER: NIO -> BTC ->ETH ->XRP ->ADA ->JKS ->SPWR ->AAPL
initial_weight = np.array([0.1201,0.254,0.122,0.072,0.410,0.007,0.004,0.007])


#Loding previous dataset
df = pd.read_csv("./history/prices.csv")

#Cryptos
url = "https://api.nomics.com/v1/currencies/ticker?key=41f2e495a3e8012cf8bcd2cb38626651&ids=BTC,ETH,XRP,ADA&interval=1d"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

for i in range(len(data)):
    new_data[data[i]["currency"]] = data[i]["price"]
    


#Stocks
stocks = ['AAPL','NIO','JKS', 'SPWR']

#Get all prices into a dataframe
for stock in stocks: 
    prices = requests.get(f'https://financialmodelingprep.com/api/v3/profile/{stock}?apikey=8648d46b7ae4fa07c7ecd3b90861c94e').json()

    new_data[stock] = float(prices[0]["price"])

new_data["Date"] = today
df = df.append(new_data, ignore_index=True)
df = df.set_index("Date")

#saving new dataset    
df.to_csv("./history/prices.csv")

