#!/usr/bin/env python
# coding: utf-8

# In[3]:


dic = {}
N = int(input())
for i in range(N):
    lis = input().split()
    dic[lis[0]] = (float(lis[1])+float(lis[2])+float(lis[3]))/3
    
x = dic[input()]
print('{:.2f}'.format(x))


# In[ ]:




