#!/usr/bin/env python
# coding: utf-8

# In[15]:


import schedule
import time
from datetime import datetime as dt
from automated_data import getData
from automated_anaysis import getAnalysis

def updateData():
    getData()

def portfolioAnalysis():
    getAnalysis()
    print("Analysis has been conducted")

#getting data updated
schedule.every().monday.at("22:00").do(updateData)
schedule.every().tuesday.at("22:00").do(updateData)
schedule.every().wednesday.at("22:00").do(updateData)
schedule.every().thursday.at("22:00").do(updateData)
schedule.every().friday.at("22:00").do(updateData)

#getting 
schedule.every().sunday.at("22:30").do(portfolioAnalysis)



while True:
    schedule.run_pending()
    time.sleep(30)

