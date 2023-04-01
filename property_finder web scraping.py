#!/usr/bin/env python
# coding: utf-8

# In[9]:


#importing libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[10]:


l=[]
#headers for the website
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
#url for the website
base_url='https://www.propertyfinder.eg/en/search?c=1&ob=mr&page='

for page in range(1,51):                    #number of pages
    r=requests.get(base_url+str(page),headers=headers)  #connecting to website
    c=r.content
    soup=BeautifulSoup(c,'html.parser') #extract html code for the website
    all=soup.find_all('div',{'class':'card-list__item'})  #card which contains all tags
    #extract text in all tags 
    for tag in all:
        d={}
        d['Property_Type']=tag.find('p',{'class':'card-intro__type'}).text.strip()
        d['Price']=tag.find('p',{'class':'card-intro__price'}).text.strip().replace(' ','').replace('\n','')
        d['Title']=tag.find('h2',{'class':'card-intro__title'}).text.strip()
        d['Location']=tag.find('span',{'class':'card-specifications__location-text'}).text.strip()
        d['Description']=tag.find('div',{'class':'card-specifications__amenities'}).text.strip().replace(' ','').replace('\n',',')
        d['Time']=tag.find('p',{'class':'card-footer__publish-date'}).text.strip()
        #extract text from inside pages
        url='https://www.propertyfinder.eg'+tag.find('a').attrs['href']
        r2=requests.get(url,headers=headers)
        c2=r2.content
        soup2=BeautifulSoup(c2,'html.parser')
        
        try:
            d['Amenities']=soup2.find('div',{'class':'property-amenities'}).text.strip().replace('\n',',')
            
        except:
            d['Amenities']='none'
        print('\n')
        l.append(d)           #adding dictionary to list


# In[11]:


len(l)


# In[12]:


df=pd.DataFrame(l)  #exporting data to csv file
df.to_csv('E:\DATA ANALYSIS ITI\projects\web scraping\property_finder.csv')


# In[ ]:




