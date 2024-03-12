#!/usr/bin/env python
# coding: utf-8

# # Importing necessary libraries

# In[73]:


import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[74]:


df=pd.read_csv('DailyDelhiClimateTest.csv')


# In[75]:


df.head()


# In[76]:


df.tail()


# # Checking for null values

# In[77]:


df.isnull().sum()


# # Checking for duplicates

# In[78]:


df.duplicated(subset=None, keep='first')


# Checking the datatype

# In[79]:


df.dtypes


# # Comment: The date given above is an object and we need to convert the date into a datetime

# In[80]:


df['date']=pd.to_datetime(df['date'])


# In[81]:


df.shape


# In[82]:


df.dtypes


# # Addressing the outliers using boxplots and scatterplot

# In[83]:


sns.boxplot(df)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
#label and title
plt.xlabel('features',fontsize=10)
plt.ylabel('measure',fontsize=10)
plt.title("Box plot showing the outliers",fontsize=12)


# ## There is a outlier in the mean pressure

# In[84]:


from scipy import stats


# In[85]:


Q1=df['meanpressure'].quantile(0.25)
Q3=df['meanpressure'].quantile(0.75)
IQR=Q3-Q1
print(IQR)


# In[86]:


# Above Upper bound
upper = Q3 + 1.5 * IQR
upper_array = np.array(df['meanpressure'] >= upper)
print("Upper Bound:", upper)
print(upper_array.sum())

# Below Lower bound
lower = Q1 - 1.5 * IQR
lower_array = np.array(df['meanpressure'] <= lower)
print("Lower Bound:", lower)
print(lower_array.sum())


# The value of the mean presure must be outside Q1-1.5*IQR This is why it is showing the outlier

# In[87]:


sns.boxplot(df['meanpressure'])


# In[88]:


# Removing the outliers
df.drop(index=upper_array.sum(), inplace=True)
df.drop(index=lower_array.sum(), inplace=True)
 
# Print the new shape of the DataFrame
print("New Shape: ", df.shape)


# In[89]:


sns.boxplot(df)


# In[90]:


df.describe()


# # I have successfully removed the outlier 

# In[93]:


# https://www.youtube.com/watch?v=VJc7SaWnESo&t=113s  
##(dealing with outliers)


# ## EDA on humidity

# In[100]:


df.set_index('date',inplace=True)


# In[104]:


df['humidity'].plot(figsize=(20,12))


# # changing the x limit,y limit

# In[114]:


df['humidity'].plot(xlim=['2017-01-01','2017-04-24'],ylim=[0,200],figsize=(12,4))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Humidity',fontsize=12)
plt.title('Humidity of City Delhi Over the first Four Months', fontsize=14)


# In[116]:


df.index


# In[119]:


date_specific_humidity=df.loc['2017-02-03':'2017-04-24']['humidity']


# In[120]:


date_specific_humidity


# In[122]:


from datetime import datetime


# In[123]:


datetime.now()


# Time Resampling

# In[151]:


df.reset_index('month',inplace=True)


# In[163]:


df.set_index('date',inplace=True)


# In[164]:


df.resample(rule='BQS').max()


# In[166]:


df.resample(rule='BQS').max().plot(kind='bar')


# In[167]:


df.resample(rule='M').max().plot(kind='bar')


# In[171]:


df['humidity:30 days rolling']=df['humidity'].rolling(30).mean()


# In[173]:


df


# In[174]:


df.drop(columns=['meanpressure:30 days rolling'],inplace=True)


# In[176]:


df.drop(columns=['Open:30 days rolling'],inplace=True)


# In[177]:


df


# In[180]:


df[['humidity','humidity:30 days rolling']].plot(figsize=(12,5))


# In[ ]:




