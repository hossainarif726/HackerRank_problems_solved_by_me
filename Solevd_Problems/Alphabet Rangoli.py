#!/usr/bin/env python
# coding: utf-8

# In[11]:


alphabet = ['a','b','c','d','e','f',
            'g','h','i','j','k','l',
            'm','n','o','p','q','r',
            's','t','u','v','w','x',
            'y','z']
N = int(input())

t = (N+(N-1))
print(t)

v = t+(t-1)

for i in range(1,(t+1)):
    print(alphabet[N-i].center(v,'-'))
    print((alphabet[N-i]+'-'+alphabet[N-(i+1)]+'-'+alphabet[N-i]).center(v,'-'))


# In[ ]:




