#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cgi
from create import main
from lib.data_table import generate_html_with_table as ghwt
from bs4 import BeautifulSoup as BS

soup = BS(open("index.html"),'html.parser')

soup.body.append(str(main("TailNumbers.eml")))

with open('index.html','w') as outf:
    outf.write(str(soup))

print(soup)

