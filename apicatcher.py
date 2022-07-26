# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import pandas as pd

#%% Via the Package
from newscatcherapi import NewsCatcherApiClient

key = '' 

newscatcherapi = NewsCatcherApiClient(x_api_key=key)

all_articles = newscatcherapi.get_search(q='Elon Musk',
                                         lang='en',
                                         countries='CA',
                                         page_size=100)

# Unpackage into data frame 
article_list = all_articles['articles']
article_df = pd.DataFrame(article_list)
#%% Via Requests
import requests

url = "https://api.newscatcherapi.com/v2/search"

querystring = {"q":"\"Elon Musk\"","lang":"en","sort_by":"relevancy","page":"1"}

headers = {
    "x-api-key": key
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

#print(response.text) 

#%% Unpack list into a data frame
