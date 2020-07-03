#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = int(input())
lis = [12,14,45]
for j in range(n):
    lis1,i,e = input().split()
    if lis1 == 'insert':
        lis.insert(int(i),int(e))
        
    elif lis1 == 'print':
        print(lis)
        
    elif lis1 == 'remove':
        lis.remove(int(i))
        
    elif lis1 == 'append':
        lis.append(int(i[i]))
        
    elif lis1 == 'sort':
        lis.sort()
        
    elif lis1 == 'pop':
        lis.pop(int(i))
        
    elif lis1 == 'reverse':
        lis.reverse()


# In[ ]:


i = input().split()
lis = [12,14,45]
if i[0] == 'insert':
    lis.insert(int(i[1]),int(i[2]))
    print(lis)


# In[ ]:




