#!/usr/bin/env python
# coding: utf-8

# # Loading our data

# In[2]:


import pandas as pd

# List of column names (copy-paste exactly — these come from the dataset description)
columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
]

# Load the file
df = pd.read_csv('adult.data',          # change to your filename if different
                 header=None,           # ← important! no header in file
                 names=columns,         # give it our column names
                 skipinitialspace=True, # removes extra spaces after commas
                 na_values=' ?')        # turns " ?" into real NaN (missing)

# Check it worked!
print(df.shape)          # should show something like (32561, 15)
df.head()                # shows first 5 rows nicely


# In[3]:


df.dtypes


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.shape


# ## How many people of each race are represented in this dataset?

# In[7]:


race_count = df['race'].value_counts()
race_count


# ## What is the average age of men?

# In[8]:


average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
average_age_men


# ## What is the percentage of people who have a Bachelor's degree?

# In[9]:


percentage_bachelors = round(df['education'].value_counts(normalize=True)['Bachelors'] * 100, 1)

percentage_bachelors


# ## What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

# In[12]:


# 1. We define who has 'advanced education'
advanced_edu = ['Bachelors', 'Masters', 'Doctorate']

# 2. We filter the data to only include these people
higher_education = df[df['education'].isin(advanced_edu)]

# 3. We count how many of these specific people earn >50K
higher_education_rich = higher_education[higher_education['salary'] == '>50K']

# 4. We calculate the percentage
percentage = (len(higher_education_rich) / len(higher_education)) * 100
print(f"Percentage: {round(percentage, 1)}%")


# ## What percentage of people without advanced education make more than 50K?

# In[13]:


# 1. We identify the people WITHOUT advanced education
# (The "~" symbol means "NOT" in Python logic)
lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

# 2. We count how many of these people earn >50K
lower_education_rich = lower_education[lower_education['salary'] == '>50K']

# 3. We calculate the percentage based on the new total
percentage = (len(lower_education_rich) / len(lower_education)) * 100
print(f"Percentage: {round(percentage, 1)}%")


# ## What is the minimum number of hours a person works per week?

# In[17]:


# This looks at the 'hours-per-week' column and finds the smallest number
min_work_hours = df['hours-per-week'].min()

print(f"The minimum work hours are: {min_work_hours}")


# ## What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

# In[18]:


# 1. We already found the minimum is 1 hour
min_work_hours = df['hours-per-week'].min()

# 2. We find everyone who works exactly 1 hour
num_min_workers = df[df['hours-per-week'] == min_work_hours]

# 3. From that small group, we find how many make >50K
rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K']

# 4. We calculate the percentage
percentage = (len(rich_min_workers) / len(num_min_workers)) * 100
print(f"Percentage: {percentage}%")


# ## What country has the highest percentage of people that earn >50K and what is that percentage?

# In[20]:


# 1. Count how many people from each country earn >50K
rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()

# 2. Count total number of people from each country
total_by_country = df['native-country'].value_counts()

# 3. Divide the rich count by the total count to get the percentage
country_percentages = (rich_by_country / total_by_country) * 100

# 4. Find the country with the highest value
highest_country = country_percentages.idxmax()
highest_percentage = round(country_percentages.max(), 1)

print(f"Highest Country: {highest_country} with {highest_percentage}%")


# ## Identify the most popular occupation for those who earn >50K in India.

# In[22]:


# 1. First sieve: Only keep people from India
india_df = df[df['native-country'] == 'India']

# 2. Second sieve: From that group, only keep those who earn >50K
india_rich = india_df[india_df['salary'] == '>50K']

# 3. Count the jobs and find the top one
top_job = india_rich['occupation'].value_counts().idxmax()

print(f"The most popular job for high-earners in India is: {top_job}")

