#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# In[ ]:





# In[10]:


relationship_satisfaction_distribution = data['RelationshipSatisfaction'].value_counts()
relationship_satisfaction_distribution.plot(kind='bar')
plt.title('Relationship Satisfaction Distribution')
plt.ylabel('Number of Employees')
for i, v in enumerate(relationship_satisfaction_distribution):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')
plt.show()


# In[ ]:





# In[11]:


high_job_satisfaction_count = data[data['JobSatisfaction'] >= 4].shape[0]
plt.bar(['High Job Satisfaction'], [high_job_satisfaction_count])
plt.title('Count of Employees with High Job Satisfaction')
plt.ylabel('Number of Employees')
plt.text(0, high_job_satisfaction_count, str(high_job_satisfaction_count), ha='center', va='bottom')
plt.show()


# In[ ]:





# In[26]:


work_life_balance_count = data['WorkLifeBalance'].value_counts(normalize=True) * 100
plt.bar(work_life_balance_count.index.astype(str), work_life_balance_count)
plt.title('Work Life Balance Distribution')
plt.ylabel('Percentage')
for i, v in enumerate(work_life_balance_count):
    plt.text(i, v + 0, f'{v:.2f}%', ha='center', va='bottom')
plt.show()


# In[ ]:





# In[25]:


training_effect = data.groupby('TrainingOpportunitiesTaken')['JobSatisfaction'].mean()
training_effect.plot(kind='bar')
plt.title('Job Satisfaction vs. Training Opportunities Taken')
plt.ylabel('Average Job Satisfaction')
for i, v in enumerate(training_effect):
    plt.text(i, v + 0.0, f'{v:.4f}', ha='center', va='bottom')
plt.show()


# In[ ]:





# In[14]:


self_rating_distribution = data['SelfRating'].value_counts()
self_rating_distribution.plot(kind='bar')
plt.title('Self Rating Distribution')
plt.ylabel('Number of Employees')
for i, v in enumerate(self_rating_distribution):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')
plt.show()


# In[ ]:





# In[15]:


self_rating_distribution = data['SelfRating'].value_counts()
self_rating_distribution.plot(kind='bar')
plt.title('Self Rating Distribution')
plt.ylabel('Number of Employees')
for i, v in enumerate(self_rating_distribution):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')
plt.show()


# In[ ]:





# In[16]:


relationship_satisfaction_distribution = data['RelationshipSatisfaction'].value_counts()
relationship_satisfaction_distribution.plot(kind='bar')
plt.title('Relationship Satisfaction Distribution')
plt.ylabel('Number of Employees')
for i, v in enumerate(relationship_satisfaction_distribution):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')
plt.show()


# In[ ]:





# In[17]:


low_env_satisfaction_count = data[data['EnvironmentSatisfaction'] < 3].shape[0]
plt.bar(['Low Environment Satisfaction'], [low_env_satisfaction_count])
plt.title('Count of Employees with Low Environment Satisfaction')
plt.ylabel('Number of Employees')
plt.text(0, low_env_satisfaction_count, str(low_env_satisfaction_count), ha='center', va='bottom')
plt.show()


# In[ ]:





# In[18]:


mean_manager_rating = data['ManagerRating'].mean()
plt.bar(['Average Manager Rating'], [mean_manager_rating])
plt.title('Average Manager Rating')
plt.ylabel('Rating Level')
plt.text(0, mean_manager_rating, f'{mean_manager_rating:.2f}', ha='center', va='bottom')
plt.show()


# In[ ]:





# In[19]:


dissatisfied_employees_count = data[data['JobSatisfaction'] < 3].shape[0]
plt.bar(['Dissatisfied Employees'], [dissatisfied_employees_count])
plt.title('Count of Dissatisfied Employees')
plt.ylabel('Number of Employees')
plt.text(0, dissatisfied_employees_count, str(dissatisfied_employees_count), ha='center', va='bottom')
plt.show()


# In[ ]:





# In[27]:


training_satisfaction_distribution = data['TrainingOpportunitiesWithinYear'].value_counts()

plt.bar(training_satisfaction_distribution.index.astype(str), training_satisfaction_distribution)
plt.title('Training Opportunities Distribution')
plt.ylabel('Number of Employees')
for i, v in enumerate(training_satisfaction_distribution):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')
plt.show()


# In[ ]:





# In[30]:


plt.scatter(data['RelationshipSatisfaction'], data['ManagerRating'])
plt.title('Relationship Satisfaction vs. Manager Rating')
plt.xlabel('Relationship Satisfaction')
plt.ylabel('Manager Rating')
for i in range(len(data)):
    plt.text(data['RelationshipSatisfaction'][i], data['ManagerRating'][i], str(data['ManagerRating'][i]), fontsize=8)
plt.show()


# In[33]:


print('mahmoud')


# In[ ]:



