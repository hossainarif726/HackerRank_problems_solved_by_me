#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())

lis = []

for i in range(N):
    lis1 = []
    name = input()
    grade = float(input())
    lis1.append(name)
    lis1.append(grade)
    lis.append(lis1)

s = lis[0][1]

for i in range(len(lis)):
    if lis[i][1] < s:
        s = lis[i][1] 

for i in range(len(lis)):
    while s in lis[i]:
        lis[i].remove(s)
        
for i in range(len(lis)):
    if len(lis[i]) != 2:
        continue
    else:
        s = lis[i][1]
        break
        
for i in range(len(lis)):
    if len(lis[i]) != 2:
        continue
    else:
        if lis[i][1] < s:
            s = lis[i][1]
namlis = []
for i in range(len(lis)):
    if len(lis[i]) != 2:
        continue
    while s in lis[i]:
        namlis.append((lis[i][0]))
        break
        
namlis.sort()

for i in namlis:
    print(i)

