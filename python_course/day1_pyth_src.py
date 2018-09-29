
# coding: utf-8

# **DAY 1 - PYTHON COURSE**
# 
# Notes :\\
# 24/9/2018
# Course 1
# *************
# Inside jupyter notebook
#  
# ESC  -> command window (like vim)
# 	a(bove)
# 	b(elow)
# 	
# CTRL + ENTER or SHIFT + ENTER 	-> Exec.
# (stays here)    (goes next shell)77
# 
# ESC -> X (delete shell) 
# 
# ESCP -> (m/w) (switches from code to markdown)
# 
# 
# 

# In[1]:


print(42)


# In[2]:


import mne
import pandas as pd
import sklearn


# In[6]:


l1 = [41,40,39]
l2 = [1,2,3]
for (i, j) in zip (l1, l2):
    print(j+i)


# In[7]:


for (i, j) in enumerate (l1):
    print((j,i))


# In[15]:


2 + 40


# In[11]:


import pandas


# In[14]:


w, W = 60, 18
print(w - W)


# In[16]:


type(w)


# In[28]:


import numpy as np


# In[34]:


#need to place folder data in home directory.
data = np.loadtxt(
    fname='/home/tyler/python-novice-inflammation-data/data/inflammation-01.csv', 
    delimiter = ',')


# In[35]:


print(data)


# In[36]:


type(data)
data.dtype


# In[37]:


data.shape


# In[38]:


data[0, 0]


# In[46]:


get_ipython().system('pwd')


# In[53]:


get_ipython().system('[a]')


# In[54]:


data[0:4, 0:10]


# In[55]:


data[5:10, 0:10]


# In[56]:


data[5:10, :10]


# In[59]:


doubledata = data * 2.0


# In[60]:


print('double', doubledata)


# In[61]:


np.mean(data)


# In[62]:


np.max(data), np.min(data), np.std(data)


# In[63]:


data.max(), data.min(), data.std()


# In[64]:


daily_avg = np.mean(data, axis=0)


# In[65]:


print(daily_avg)


# In[66]:


daily_avg.shape


# In[68]:


patient_max = np.max(data, axis = 1)
print(patient_max)


# In[70]:


import matplotlib.pyplot as plt


# In[71]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[74]:


plt.imshow(data)
plt.colorbar()


# In[77]:


plt.plot(daily_avg)
plt.savefig('daily_avg.png')


# # Recap NumPy

# In[84]:


import numpy as np
mydata = 42
print(mydata)
type(data)
data.dtype
data[1, 2]
data[5:10, 2:6]
data.mean(axis=0)


# Useful Idea for Fast code : Broadcasting

# # Loops

# In[86]:


word = 'oxygen'


# In[87]:


for letter in word:
    print(letter)


# In[88]:


len(word)


# In[90]:


letter = 'z'
for letter in 'akala':
    print(letter)
print('afterwards, ', letter)


# In[91]:


for ii, letter in enumerate(word):
    print(letter, 'is the ', ii + 1, 'th letter')


# In[93]:


city = 'Bremen'
for cc, ww in zip(city, word):
    print(cc, ww)


# In[95]:


for n in range(5):
    print(n)


# In[96]:


for n in range(3, 6):
    print(n)


# In[97]:


for n in range(3,12,4):
    print(n)


# # Lists

# In[99]:


odds = [1, 3, 5, 7, 9]
print(odds)
type(odds)


# In[100]:


# Circular in numpy.
print('last:', odds[-1])


# In[101]:


names = ['Curie', 'Einstein', 'Turing']
print(names)


# In[103]:


names[1] = 'Darwin'
print(names)


# In[104]:


print(names[1][2])


# In[108]:


mylist = [1, 'akala', data]


# In[110]:


mylist


# In[111]:


for item in enumerate(word):
    print(item)


# In[112]:


word


# In[113]:


word[::-1]


# In[114]:


'akalamalaka'


# In[115]:


'akalamalaka'[::-1]


# In[116]:


word + word


# In[119]:


'akala' + 'm' + 'akala'[::-1]


# In[118]:


mylist + ['mylist']


# In[120]:


word * 2


# # If/else

# In[121]:


num = 42
if num > 31:
    num


# In[123]:


if num > 23:
    print(42)
else:
    print(41)


# In[125]:


if num > 100:
    print('a')
elif num == 42:
    print('f')
else:
    print('e')
    


# In[126]:


if '':
    print('empty is true')
if 'akala':
    print('akala is true')


# In[127]:


if []:
    print('empty')
if [1,2,3]:
    print('length>0')


# In[128]:


if 0:
    print('0 is true')
if 1:
    print('1 is true')
if -1:
    print('-1 is true')


# In[130]:


if True:
    print(False)


# # Functions

# In[131]:


def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))


# In[132]:


fahr_to_celsius(12)

