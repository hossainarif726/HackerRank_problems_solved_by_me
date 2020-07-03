#!/usr/bin/env python
# coding: utf-8

# In[4]:


def split_and_join(line):
    line = line.split()
    return '-'.join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

