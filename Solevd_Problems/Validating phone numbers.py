#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
N = int(input())

for _ in range(N):
    st = input()
    s = re.findall('^[789]\d{9}$',st)
    if s:
        print('YES')
    else:
        print('NO')


# In[ ]:




