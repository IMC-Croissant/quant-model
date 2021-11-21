#!/usr/bin/env python
# coding: utf-8

# # Calculation of Portfolio Volatility
# ![](mm2-variance.gif)

# ### 1. Environment

# In[2]:


import datetime as dt
import json
import numpy as np
import pandas as pd
import requests


# In[6]:


get_ipython().run_line_magic('pip', 'install requests')


# ### 2. Preliminaries
# API used: https://eodhistoricaldata.com

# In[72]:


key_US = '619a0bff3eb4f3.04814042'
key = '619a4293043562.72616470'
start = dt.date.today() - dt.timedelta(366)
symbols = "TSLA.US BHP.LSE PLUG.US RDSB.LSE UMI.BR ENGI.PA ENR.XETRA CUR.V".split()
weights = np.array([12.5,12.5,12.5,12.5,12.5,12.5,12.5,12.5]) / 100
data = []


# ### 3. Download and prepare data

# In[74]:


#date in different exchanges is different
for symbol in symbols:
    request = f"https://eodhistoricaldata.com/api/eod/{symbol}?api_token={key}&from={start}&fmt=json"
    raw =requests.get(request).text
    raw = pd.DataFrame(json.loads(raw))
    data.append(raw['close'])
data = pd.DataFrame(data).T
data.columns = symbols
data.index = raw['date']
data.head()    


# In[77]:


raw.tail(10)


# In[ ]:


new_set=data.dropna()


# In[84]:


new_set


# ### 4. Calculate instaneous returns

# In[66]:


returns = np.log(new_set).diff()
returns.dropna(inplace = True)
trading_day = len(returns)
std = np.sqrt(returns.var() * trading_day)
print(f"{std.mean():.2%}")


# ### 5. Equal Weighted Portfolio Volatility 

# In[67]:


cov = returns.cov() * trading_day
print(f"{np.sqrt(np.dot(weights.T, np.dot(cov, weights))):.2%}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




