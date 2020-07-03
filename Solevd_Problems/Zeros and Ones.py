#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy
a,b,c = map(int,input().split())
print(numpy.zeros((a,b,c),int))
print(numpy.ones((a,b,c),int))


# In[10]:


import numpy
a = input().strip().split()
b = numpy.array(a,int)
print(numpy.zeros((b),int))
print(numpy.ones((b),int))


# In[ ]:




