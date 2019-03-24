#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cgi
from create import main
from bs4 import BeautifulSoup as BS

soup = BS(open("index.html"),'html.parser')

with open('index.html','w') as outf:
    outf.write(str(soup))

print(soup) 

