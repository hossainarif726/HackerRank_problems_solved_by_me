#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = int(input())

if n % 2 != 0:
    print('Weird')
    
elif n > 1 and n < 6:
    print('Not Weird')
    
elif n > 5 and n < 21:
    print('Weird')
    
else:
    print('Not Weird')

