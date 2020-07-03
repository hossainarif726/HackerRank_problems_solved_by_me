#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = int(input())
lis = input().split()
for i in range(len(lis)):
    lis[i] = int(lis[i])
    
t = tuple(lis)
print(hash(t))


# In[ ]:




