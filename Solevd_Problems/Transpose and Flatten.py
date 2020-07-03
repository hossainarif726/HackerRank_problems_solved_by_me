#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy
N,M = map(int,input().split())
lis = []
for i in range(N):
    lis.append(input().strip().split())
p = numpy.array(lis,int)
print(p.transpose())
print(p.flatten())


# In[ ]:




