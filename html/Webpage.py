#!/usr/bin/env python
# coding: utf-8

# In[35]:


import cgi
import bs4
from bs4 import BeautifulSoup as BS

soup = BS(open("xd.html"),'html.parser')

with open('index.html','w') as outf:
    outf.write(str(soup))

print(soup)

