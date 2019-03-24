#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def main(filename):

    file = open(filename)
    content = np.array(file.readlines())
    file.close()

    counter = 0
    start = 0
    end = 0
    gotems = 0
    prev = '\n'
    test = np.array(['\n','\n','\n','\n','\n','\n'])
    
    for i,curr in enumerate(content):
        if curr == '\n' and curr == prev:
            counter +=1
            start = i
            break
        prev = curr
    new = np.array(content[start+1:])
    for i,curr in enumerate(new):
        currtest = np.array(new[i:i+6])
        if np.array_equal(currtest, test):
            gotems += 1
        elif len(currtest[0]) > 9:
            end = start+i
            break
    content = np.array(content[start+1:end-2])
    content = np.where(content== '\n',content,np.char.strip(content,'\n'))
    delete = []
    for i,curr in enumerate(content):
        if curr == '\n':
            delete.append(i)
    content = np.delete(content,delete)
    new = np.array(content)
    i = 0
    while i < content.size:
        currtest = np.array(content[i:i+7])
        try:
            test = int(currtest[6])
            new = np.insert(new, i+3, 'no tail number')
            content = new
            newcurrtest = np.array(content[i:i+7])
        except (TypeError, ValueError):
            i+=7
            continue
        i+=7
    i=0
    new = np.empty((7,))
    while i < content.size:
        new = np.vstack((new,content[i:i+7]))
        i+=7
    content = np.array(new[1:])
    tomp = []
    for i,a in enumerate(content):
        temp = []
        for j,b in enumerate(a):
            if j is 0:
                temp.append(int(b))
            if j is 1:
                temp.append(b)
            if j is 2:
                temp.append(b)
            if j is 3:
                temp.append(b)
            if j is 4:
                temp.append(int(b))
            if j is 5:
                temp.append(b)
            if j is 6:
                temp.append(b)
        tomp.append(temp)
    return(np.array(tomp))

