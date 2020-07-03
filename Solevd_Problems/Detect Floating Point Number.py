#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
T = int(input())

for i in range(T):
    N = input()
    st = re.findall('^[+-]?\d*\.\d+$',N)
    print(bool(st))


# In[ ]:




