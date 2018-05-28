
# coding: utf-8

# In[136]:


list=[]
for i3 in range(0,1000):
    s=3*i3
    if s<1000:
        list.append(s)

for i5 in range(0,1000):
    s=5*i5
    if s % 3!=0:
        if s<1000:
            list.append(s)
#print(list)

x=sum(list)

print(x)
        


