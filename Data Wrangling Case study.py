#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Reading the data from url

# In[2]:


url='https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv'
df=pd.read_csv(url)


# ### High Level Data Understanding

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape       # finds the number of rows and columns (rows,column)


# In[6]:


df.describe()   


# In[7]:


df.info()


# In[8]:


df.dtypes     #gives data types of column


# ### Low Level Data Understanding 

# In[9]:


df['location'].nunique()   #gives count of unique values in location column


# In[10]:


df['continent'].value_counts()


# In[11]:


df['total_cases'].max()


# In[12]:


df['total_cases'].mean()


# In[13]:


print("25%,50% & 75% quartile value in 'total_deaths' : \n",df['total_deaths'].describe()[4:7])


# In[14]:


df.groupby(['human_development_index','continent']).human_development_index.max().tail(1)


# In[15]:


df.groupby(['gdp_per_capita','continent']).gdp_per_capita.min().tail(1)


# ### Filter the dataframe with only this columns

# In[16]:


df = df[['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']]


# In[17]:


df


# ### Data Cleaning

# In[18]:


df.drop_duplicates()        # Removes teh duplicate values


# In[19]:


df.isnull().sum()   #finds the missing values


# In[20]:


df['continent'].isnull().sum()


# In[21]:


df_remove=df.copy()
df_remove=df_remove.dropna(subset=['continent'])


# In[22]:


df_remove


# In[23]:


df_fill=df.fillna(0)


# In[24]:


df_fill


# ### Date time format 

# In[25]:


df['date']=pd.to_datetime(df['date'])


# In[26]:


df


# In[27]:


df['month'] = df['date'].dt.month


# In[28]:


df.head()


# ### Data Aggregation

# In[29]:


df_groupby = df.groupby(by='continent')
df_groupby.max()


# ### Feature Engineering 

# In[30]:


df['total_deaths_to_total_cases'] = df['total_deaths']/df['total_cases']
df.head()


# ### Data Visualization 

# In[32]:


sns.distplot(a=df['gdp_per_capita'],color='red')


# In[33]:


sns.scatterplot(x=df['total_cases'],y=df['gdp_per_capita'])


# In[ ]:


sns.pairplot(df)


# In[ ]:


sns.catplot(x='continent', y='total_cases',data=df,hue='total_deaths',kind='bar',height = 1)


# In[ ]:


plt.figure(figsize=(10,17))
sns.catplot(data=df_groupby,x='continent',y='total_cases',kind='bar')
plt.xticks(rotation=90)
plt.show()


# ### Save the df_groupby dataframe in your local drive using pandas.to_csv function¶

# In[ ]:


df_groupby.to_csv('New-df-groupby')


# In[ ]:




