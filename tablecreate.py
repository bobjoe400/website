#!/usr/bin/env python
# coding: utf-8

# In[3]:

import numpy as np

def createtable():
    data = np.load('data.npy')
    s = '''        <table>
                    <tr>
                        <th>Line #</th>
                        <th>Plane Type</th>
                        <th>order1</th>
                        <th>Tail #</th>
                        <th>order2</th>
                        <th>airline1</th>
                        <th>airline2</th>
                    </tr>'''
    for i in data:
        s+='<tr>'
        for j in i:
            s+='<td>'+j+'</td>'
        s+='</tr>'
    s+='</table>'
    return s

