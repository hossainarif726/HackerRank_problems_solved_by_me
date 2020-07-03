#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = list(map(int,input().split()))
b = list(map(int,input().split()))

from itertools import product

a.sort()
b.sort()

z = list(product(a,b))
for i in z:
    print(i,end=' ')

