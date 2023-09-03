#!/usr/bin/env python
# coding: utf-8

# In[191]:


text="Hello my name is shashvat Ahuja"


# In[192]:


text


# In[193]:


alpha="abcdefghijklmnopqrstuvwxyz"
alpha=list(alpha)


# In[ ]:





# In[194]:


keys={}
for i in range(26):
    keys[alpha[i]]=i


# In[195]:


for i in range(10):
    keys[str(i)]=26+i


# In[196]:


def encryp(text):
    encrypted=""
    for i in range(len(text)):
        if text[i]==" ":
            encrypted+=" "
            continue
        if text[i].isupper():
            encrypted+="#"
            continue
        encrypted+=chr((keys[text[i]]+5)%26+ord("a"))
    return encrypted


# In[197]:


encryp(text)


# In[203]:


def decryp(text):
    dencrypted=""
    for i in range(len(text)):
        if text[i]==" ":
            dencrypted+=" "
            continue
        if text[i]=="#":
            dencrypted+=(chr((keys[text[i+1]]-5)%26+ord("a"))).upper()
            continue
        dencrypted+=chr((keys[text[i]]-5)%26+ord("a"))
    return dencrypted


# In[204]:


decryp(encryp(text))


# In[200]:


"t".upper()


# In[ ]:




