#!/usr/bin/env python
# coding: utf-8

# In[6]:


def mutate_string(string,position,character):
    return string[:position]+character+string[position+1:]

if __name__ == '__main__':
    S = input()
    i,c = input().split()
    print(mutate_string(S,int(i),c))


# In[ ]:




