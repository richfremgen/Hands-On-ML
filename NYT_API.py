#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 10:47:33 2022

@author: richardfremgen
"""

#%% Packages
import requests as req
import time
import pandas as pd 
#%%
def get_nyt_data(num, TOPIC):
    
    articles = []
    base_link = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?'
    b_l = base_link + TOPIC  
    
    API_KEY=
 
    for i in range(num): 
        
        url=b_l+'&api-key='+API_KEY+'&page='+str(i)+'&sort=newest'
        response = req.get(url).json() 
        docs = response['response']['docs'] 
        
        if len(docs) == 0:
            break 
        
        for doc in docs:
            filteredDoc = {}
            filteredDoc['date'] = doc['pub_date']
            filteredDoc['type'] = doc['document_type']
            try:
                filteredDoc['sec'] = doc['section_name'] 
            except KeyError:
                filteredDoc['source'] = None 
            try:
                filteredDoc['sub_sec'] = doc['subsection_name']
            except KeyError:
                filteredDoc['sub_sec'] = None
            filteredDoc['news_desk'] = doc['news_desk'] 
            try:
                filteredDoc['source'] = doc['source'] 
            except KeyError:
                filteredDoc['source'] = None
            filteredDoc['title'] = doc['headline']['main']
            filteredDoc['abstract'] = doc['abstract']
            filteredDoc['paragraph']=doc['lead_paragraph']
            filteredDoc['url']=doc['web_url']
            articles.append(filteredDoc)
            
        print('Completed Page:' + str(i))
                            
        # Avoid hitting the API request limit.
        if i == max(range(num)) or len(docs) < 10:
            break
        else:
            time.sleep(6) 
            
    print('No. of Articles:' + str(len(articles)))
    df = pd.DataFrame(articles) 
    print('All done!')
    return(df)

#%% Circular Economy
ce = 'fq=headline:"circular economy" OR abstract:"circular economy" OR body:"circular economy"' 
#test2 = 'fq=headline:"circular economy"' 
b = get_nyt_data(10, ce) 
#b.to_excel('test.xlsx', index=False)  

#%% Date Stuff 
b['year'] = pd.DatetimeIndex(b['date']).year

save_yr = b.groupby(by='year')['year'].count()

import matplotlib.pyplot as plt
#import seaborn as sns

# pivot the data and aggregate
dfp = b.pivot_table(index='year', aggfunc='size')

# plot 
plt.style.use('seaborn-whitegrid')
fig = plt.figure()
plt.xticks(fontsize=16, fontweight='bold')
plt.yticks(fontsize=16, fontweight='bold')
dfp.plot(kind='bar', figsize=(20, 8), rot=0, color='darkblue') 
plt.xlabel(None)
fig.suptitle('NYT Circular Economy Mentions', 
             fontsize=30, style = 'italic', fontweight='bold')
plt.show()
 

#%%
# How to search for two different fields
test = 'fq=news_desk:"Culture" AND section_name:"Movies"'
b = get_nyt_data(1, test) 
#a.to_excel('test.xlsx', index=False) 
# b_d = '20220101'
# e_d = '20220430'
# date_rge= '&begin_date='+b_d+'&end_date='+e_d 
#hline = 'fq=headline:'
#hline = 'fq=' 
# url=base_link+TOPIC+'&api-key='+API_KEY+'&page='+str(i)+date_rge  

#%% Biomethane Search
bio = 'fq="biomethane"'
#test2 = 'fq=headline:"circular economy"' 
c = get_nyt_data(2, bio) 
#c.to_excel('test.xlsx', index=False)