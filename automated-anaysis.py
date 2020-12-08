#!/usr/bin/env python
# coding: utf-8

# In[18]:


from datetime import date
import urllib.request
import requests
import pandas as pd
import json
import numpy as np
from send_email import sendEmail

today = date.today()
new_data= {}

#Initial portfolio weights: ORDER: NIO -> BTC ->ETH ->XRP ->ADA ->JKS ->SPWR ->AAPL
initial_weight = np.array([0.1201,0.254,0.122,0.072,0.410,0.007,0.004,0.007])


#Loding previous dataset
df = pd.read_csv("./history/prices.csv")

#converting date to index
df = df.set_index("Date")

#make sure everyseries is of type float
for column in df.columns:
    df[column] = df[column].astype(float)

    
#calculating percentage change
return_stocks = df.pct_change()

number_of_portfolios = 2000 #2000 simulated portfolios
RF = 0 #return on risk-free asset


portfolio_returns = []
portfolio_risk = []
sharpe_ratio_port = []
portfolio_weights = []

#iterating over each portfolio simulation
for portfolio in range (number_of_portfolios):
    
    #generate a w random weight of lengt of number of stocks
    weights = np.random.random_sample((len(df.keys())))
 
    weights = weights / np.sum(weights)
    annualize_return = np.sum((return_stocks.mean() * weights) * 252)
    portfolio_returns.append(annualize_return)
    #variance
    matrix_covariance_portfolio = (return_stocks.cov())*252
    portfolio_variance = np.dot(weights.T,np.dot(matrix_covariance_portfolio, weights))
    portfolio_standard_deviation= np.sqrt(portfolio_variance) 
    portfolio_risk.append(portfolio_standard_deviation)
    #sharpe_ratio
    sharpe_ratio = ((annualize_return- RF)/portfolio_standard_deviation)
    sharpe_ratio_port.append(sharpe_ratio)

    portfolio_weights.append(weights)

portfolio_risk = np.array(portfolio_risk)
portfolio_returns = np.array(portfolio_returns)
sharpe_ratio_port = np.array(sharpe_ratio_port)

porfolio_metrics = [portfolio_returns,portfolio_risk,sharpe_ratio_port, portfolio_weights] 

portfolio_dfs = pd.DataFrame(porfolio_metrics)
portfolio_dfs = portfolio_dfs.T
portfolio_dfs.columns = ['Port Returns','Port Risk','Sharpe Ratio','Portfolio Weights']

#convert from object to float the first three columns.
for col in ['Port Returns', 'Port Risk', 'Sharpe Ratio']:
    portfolio_dfs[col] = portfolio_dfs[col].astype(float)

#portfolio with the highest Sharpe Ratio
Highest_sharpe_port = portfolio_dfs.iloc[portfolio_dfs['Sharpe Ratio'].idxmax()]
#portfolio with the minimum risk 
min_risk = portfolio_dfs.iloc[portfolio_dfs['Port Risk'].idxmin()]

#Highest_sharpe_port
#print(Highest_sharpe_port)
#print(min_risk)

#Summarizing Optimal Action to take
max_sharpe_port = pd.Series((Highest_sharpe_port["Portfolio Weights"])*100, index=df.keys())
min_risk_port = pd.Series((min_risk["Portfolio Weights"])*100, index=df.keys())


#creating a summary recommendation table
summary_table = pd.DataFrame(columns=[max_sharpe_port.index])
summary_table.loc["current_position"] = initial_weight*100
summary_table.loc["max_sharpe_port"] = max_sharpe_port.values
summary_table.loc["min_risk_port"] = min_risk_port.values

summary_table = summary_table.round(2)
print(summary_table)

sendEmail("joao.fragoso.januario@gmail.com","Weekly Portfolio Update {}".format(str(today.strftime("%d %b, %Y"))),summary_table.T)

