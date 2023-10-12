#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing laibraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[ ]:



lst=[]                  #list of data
#list of all links
links=[]

num_page=1
while True:
    #header for the web site
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    #url for the website
    url=f'https://www.olx.com.eg/properties/?page={num_page}'
    print(url)
    #connecting to web site
    result = requests.get(url, headers=headers)
    #content of the web site
    src = result.content
    #html code for the web site
    soup = BeautifulSoup(src, "lxml")
    #scraping links in each link
    links_in_page=soup.find_all('div',{'class':'_41d2b9f3'})
    #print(links_in_page)
    #scraping links for each url
    for i in links_in_page:
        l='https://www.olx.com.eg'+i.find('a').attrs['href']
        links.append(l)
    #condition which counter will stop
    next_page=soup.find('div',{'title':'التالي'}) 
    if next_page!= None:
        num_page+=1
    else:
        print('done')
        break
#scraping data from each link
for link in links:
    d={}
    d['link']=link
    print(link)
    d['web_name']='olx'
    d['source']='scraping'
    response=requests.get(link,headers=headers)
    text=response.content
    soup2=BeautifulSoup(text,'html.parser')
    try:
        d['rent_sale']=soup2.find_all('a',{'class':'_151bd34b'})[2].text.partition(' ')[-1]
        print(soup2.find_all('a',{'class':'_151bd34b'})[2].text.partition(' ')[-1])
    except:
        d['rent_sale']=None
        print(d['rent_sale'])
    try:
        d['description']=soup2.find('div',{'class':'_0f86855a'}).text
        print(soup2.find('div',{'class':'_0f86855a'}).text)
    except:
        d['description']=None
        print(d['description'])
    try:        
        d['city']=soup2.find('span',{'class':'_8918c0a8'}).text.partition(', ')[2].strip()
        print(d['city'])
    except:
        d['city']=None
        print(d['city'])
    try:        
        d['location2']=soup2.find('span',{'class':'_8918c0a8'}).text.partition(', ')[0].strip().partition('-')[0].strip()
        print(d['location2'])
    except:
        d['location2']=None
        print(d['location2'])
    try:
        location1=soup2.find('span',{'class':'_8918c0a8'}).text.partition(',')[0].partition('-')[2].strip()
        if location1=='':
            d['location1']=d['location2']
            print(d['location1'])
        else:
            d['location1']=location1
            print(d['location1'])
    except:
        d['location1']=None
        print(d['location1'])
    try:
        table2=soup2.find('div',{'class':'_241b3b1e'})        #scraping the table for each link
        table=table2.find_all('div',{'class':"b44ca0b3"})
        d['bedrooms']=None
        d['bathrooms']=None
        for n in table:
             try:
                if n.find_all('span')[0].text=='الحمامات':
                    d['bathrooms']=n.find_all('span')[1].text
                    print(n.find_all('span')[1].text)
             except:
                d['bathrooms']=None
                print(None)
             try:
                if n.find_all('span')[0].text=='غرف نوم':
                    d['bedrooms']=n.find_all('span')[1].text
                    print(n.find_all('span')[1].text)
             except:
                d['bedrooms']=None
                print(None)
             try:
                if n.find_all('span')[0].text=='النوع':
                    d['unit']=n.find_all('span')[1].text
                    print(n.find_all('span')[1].text)
             except:
                d['unit']=None
                print(None)
             try:
                if n.find_all('span')[0].text=='المساحة (م٢)':
                    d['size']=n.find_all('span')[1].text
                    print(n.find_all('span')[1].text)
             except:
                d['size']=None
                print(None)
             try:
                if n.find_all('span')[0].text=='السعر':
                    d['price']=n.find_all('span')[1].text
                    print(n.find_all('span')[1].text)
             except:
                d['price']=None
                print(None)
        
        
    except:
        pass
    lst.append(d)
    df=pd.DataFrame(lst)#exporting data to csv file
    df.to_csv(r'E:\DATA ANALYSIS ITI\projects\web scraping\olx\olx_scraping2.csv',encoding ='utf-8-sig')
    
        
        
            


# In[ ]:





# In[ ]:



    


# In[ ]:





# In[ ]:





# In[ ]:




