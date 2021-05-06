#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1

print("hello python")


# In[3]:


#2

a,b=2,3
c= a+b
d= a/b
print(c,",",d)


# In[4]:


#3

a=int(input("enter the height :"))
b=int(input("enter the base :"))

c = (a*b)/2
print("area is :",c)


# In[7]:


#4
a=int(input("enter the no1:"))
b=int(input("enter the no2 :"))
temp=a
a=b
b=temp
print("after swap",a,",",b)


# In[9]:


#5

a=int(input("enter the no:"))
import random
print(random.randint(0,a))

