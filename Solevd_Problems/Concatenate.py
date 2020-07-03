#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy
N,M,P = map(int,input().split())
lis = []
lis1 = []
for i in range(N):
    x = input().strip().split()
    lis.append(x)
for i in range(M):
    y = input().strip().split()
    lis1.append(y)
a = numpy.array(lis,int)
b = numpy.array(lis1,int)
print(numpy.concatenate((a,b)))


# In[ ]:




