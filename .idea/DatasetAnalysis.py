#!/usr/bin/env python
# coding: utf-8

# 
# # Project: Investigate a Dataset (Replace this with something more specific!)
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# This is a data set which shows th relation between differnet status and showing up in a brazilian clinic so we have diffrent states for each patient and we will find which state may affect the showing up rate for the patient at the clinic.<br>
# ### we have some important columns like:
# 1-Age<br>
# 2-Diabetes<br>
# 3-Neighbourhood<br>
# ### and other which will not affect the analysis as:
# 1-patient ID<br>
# 2-AppointmentID<br>
# 3-ScheduledDay<br>
# 
# #### Limition: patient id, appointment id, scheduleDay will not be used for analysis.
# 

# In[5]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# ### General Properties

# In[7]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
df = pd.read_csv('noshowapp.csv')
df.head()
#taking a look of the dataset


# In[8]:


df.shape
#knowing how many rows and columns


# In[9]:


df.info()
#to make sure there is no missing value


# as it shown there is no missing values here.

# In[11]:


df.describe()


# this data shows:
# 1- Average age is 37 years.
# 2- Max age is 115 years.

# 
# ### Data Cleaning (to make data more easier to deal with)

# In[43]:


df.drop(['PatientId','AppointmentID','ScheduledDay','AppointmentDay'],axis=1,inplace=True)
df.head()


# In[16]:


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.
#misspelled word correctiion
df.rename(columns={'Hipertension':'Hypertension'},inplace=True)
df.head()


# we have just rename a columns as it was misspelled.

# In[30]:


df.rename(columns={'No-show':'No_show'},inplace=True)
df.head()


# we have just rename no-show columns to make it easier for me while doing the analysis process as it gave me some bugs.

# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# ### Research Question 1 (does any disease affect showing up?)

# In[17]:


df.hist(figsize=(10,8))


# In[20]:


# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.
show=df.No_show=='No'
noshow=df.No_show=='Yes'


# In[21]:


df[show].count()


# In[22]:


df[noshow].count()


# it shows here that in general people who show up are more than who didnot nearly 4 times

# In[35]:


df.Diabetes[show].hist(alpha=0.5,label='show')
df.Diabetes[noshow].hist(alpha=0.5,label='no-show')
plt.legend()
plt.title('Showing up according to having Diabetes')
plt.xlabel('1 for Yes, 0 for No')
plt.ylabel('showing up')


# not seginficant<br>
# we cannot decide if people who have diabetes are not showing more or the people who don't have.

# In[36]:


df.Hypertension[show].hist(alpha=0.5,label='show')
df.Hypertension[noshow].hist(alpha=0.5,label='no-show')
plt.legend()
plt.title('Showing up according to having Hypertensions')
plt.xlabel('1 for Yes, 0 for No')
plt.ylabel('showing up')


# not seginficant<br>
# we cannot decide if people who have Hypertension are not showing more or the people who don't have.

# ### Research Question 2  (does recieving a SMS affect showing up? )

# In[37]:


# Continue to explore the data to address your additional research
#   questions. Add more headers as needed if you have more questions to
#   investigate.
df.SMS_received	[show].hist(alpha=0.5,label='show')
df.SMS_received	[noshow].hist(alpha=0.5,label='no-show')
plt.legend()
plt.title('Showing up according to getting a SMS')
plt.xlabel('1 for Yes, 0 for No')
plt.ylabel('showing up')


# it shows here that people who didn't get sms showed up more !!!<br>
# seginficant

# ###  Research Question 3  (does age affect showing up? )

# In[38]:


df.Age[show].hist(alpha=0.5,label='show')
df.Age[noshow].hist(alpha=0.5,label='no-show')
plt.legend()
plt.title('Showing up according to age')
plt.xlabel('age range')
plt.ylabel('showing up')


# people who are younger showed up more than older people at the clinic<br>
# for example people who are in range of 20-40 years are more showing up than who have 80-100 years<br> 
# segnificnt

# <a id='conclusions'></a>
# ## Conclusions
# 
# 1- Having disease doesnot affect showing up in the clinic at all.<br>
# 2-people who are younger are the mostly common shown at the clinic so age may affect showing up.<br>
# 3-people who doesnot get a SMS to show up are the most likely people who have already shown up at the clinic maybe there was another way to notify them to show up.

# In[ ]:




