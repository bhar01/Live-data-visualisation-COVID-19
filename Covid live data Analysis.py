#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# In[2]:


dataset_url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
df = pd.read_csv(dataset_url)
df = df[df.Confirmed > 0]
df.head()


# In[3]:


df[df.Country == 'India']


# In[4]:


fig = px.choropleth(df, locations = 'Country', locationmode = 'country names', color = 'Confirmed',animation_frame = 'Date')


# In[5]:


fig.update_layout(title_text = "Pandemic timeline")
fig.show()


# In[6]:


fig = px.choropleth(df, locations = 'Country', locationmode = 'country names', color = 'Deaths',animation_frame = 'Date')
fig.update_layout(title_text = "Pandemic timeline")
fig.show()


# In[31]:


dfind = df[df.Country == 'India']


# In[27]:


dfind = dfind[['Date','Confirmed']]
dfind['Infection Rate'] = dfind['Confirmed'].diff()
fig = px.line(dfind, x = 'Date', y = 'Infection Rate') 
fig.add_shape(
dict(
type = "line",
x0 = "2020-03-25",
y0 = 0,
x1 = "2020-03-25",
y1 = dfind['Infection Rate'].max())
)
fig.add_annotation(
dict(
    x = "2020-03-25",
    y = dfind["Infection Rate"].max()
))


# In[9]:


countries = list(df['Country'].unique())


# In[10]:


maxinf = []
for c in countries:
    max = df[df.Country == c].Confirmed.diff().max()
    maxinf.append(max)


# In[14]:


dfmi = pd.DataFrame()
dfmi['Country'] = countries
dfmi['Max infection rate'] = maxinf
dfmi.head()


# In[15]:


px.bar(dfmi, x = "Country", y = "Max infection rate", color = "Country")


# In[16]:





# In[17]:


df.head()


# In[18]:


dfind.head()


# In[54]:


dfind = df[df.Country == 'India']
dfind['Death rate']= dfind.Deaths.diff()
dfind['Infection rate']= dfind.Confirmed.diff()
dfind['Infection rate'] = dfind['Infection rate']/dfind['Infection rate'].max()
dfind['Death rate'] = dfind['Death rate']/dfind['Death rate'].max()


# In[55]:


px.line(dfind, x = "Date", y = ["Infection rate","Death rate"])


# In[ ]:




