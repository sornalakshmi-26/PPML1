#!/usr/bin/env python
# coding: utf-8

# In[1]:


f=open("D:/textfile.txt", 'w')
f.write("first line\n")
f.write("Second line\n")
f.write("third line\n")
f.close()
k=open("D:/textfile.txt", 'r')
print(k.readline())
print(k.readline())
print(k.readline())
k.close()


# In[4]:


m=open("D:/textfile.txt", 'a')
m.write("fourth line\n")
m.write("fifth line\n")
m.close()
#Open a text file in 'Read' mode t
p=open("D:/textfile.txt", 'r')
print(p.read())
p.close()


# In[5]:


import json

# JSON string
x='{"name":"John", "age":30, "city":"New York"}'

# Convert JSON string to Python dictionary
y=json.loads(x)
print(y["age"])


# In[7]:


with open("D:/textfile.txt",'r') as file:
    lines=file.readlines()
print(lines)


# In[9]:


data = {
"name": "John",
"age": 30,
"city": "New York"
}
# Convert Python dictionary to JSON string
json_data= json.dumps(data)
print(json_data)


# In[ ]:




