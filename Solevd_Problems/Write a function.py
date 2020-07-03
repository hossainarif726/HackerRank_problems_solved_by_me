#!/usr/bin/env python
# coding: utf-8

# In[8]:


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 100 != 0:
        return not leap
    
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return not leap
    
    else:
        return leap

year = int(input())
print(is_leap(year))


# In[ ]:




