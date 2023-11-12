#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly"


# In[18]:


instagram_data = pd.read_csv('instagram_data.csv', encoding='latin-1')


# In[19]:


# Display basic information about the DataFrame
print(instagram_data.info())


# In[20]:


print(instagram_data.head())


# In[21]:


print(instagram_data.describe())


# In[28]:


fig = px.histogram(instagram_data, 
                   x='Impressions', 
                   nbins=10, 
                   title='Distribution of Impressions')
fig.show()


# In[29]:


# Correlation matrix to understand relationships between numerical features
corr_matrix = instagram_data.corr()
fig_corr = go.Figure(data=go.Heatmap(z=corr_matrix.values,
                                     x=corr_matrix.columns,
                                     y=corr_matrix.index,
                                     colorscale='Viridis',
                                     zmin=-1,
                                     zmax=1))
fig_corr.update_layout(title='Correlation Matrix',
                       xaxis_title='Features',
                       yaxis_title='Features')


# In[30]:


# Explore engagement metrics using scatter plots
fig_scatter = px.scatter(instagram_data, x='Likes', y='Comments', color='Shares', size='Profile Visits',
                         title='Engagement Metrics')
fig_scatter.show()


# In[32]:


# Display top 10 captions
N = 10

# Aggregate reach metrics by summing for each caption
reach_by_caption = instagram_data.groupby('Caption').agg({
    'From Home': 'sum',
    'From Hashtags': 'sum',
    'From Explore': 'sum',
    'From Other': 'sum'
}).reset_index()

# Calculate total reach for each caption
reach_by_caption['Total Reach'] = reach_by_caption[['From Home', 'From Hashtags', 'From Explore', 'From Other']].sum(axis=1)

# Select top N captions by total reach
top_captions = reach_by_caption.nlargest(N, 'Total Reach')

# Create a bar chart for top captions
fig_top_captions = px.bar(top_captions, x='Caption', y=['From Home', 'From Hashtags', 'From Explore', 'From Other'],
                          title=f'Top {N} Captions by Total Reach')
fig_top_captions.show()


# In[42]:



fig_likes_comments_shares = px.histogram(instagram_data, x=['Likes', 'Comments', 'Shares'],
                                        title='Distribution of Likes, Comments, and Shares',
                                        labels={'value': 'Metrics', 'variable': 'Metrics'})
fig_likes_comments_shares.show()


# In[40]:


#Display proportion of engagement metrics ('Likes,' 'Comments,' 'Shares') relative to the total engagement.
fig_pie_engagement = px.pie(instagram_data, names=['Likes', 'Comments', 'Shares'],
                            title='Proportion of Engagement Metrics')
fig_pie_engagement.show()


# In[41]:


#Explore the relationship between 'Profile Visits' and 'Follows,' providing insights into user behavior after visiting the profile.
fig_profile_visits_vs_follows = px.scatter(instagram_data, x='Profile Visits', y='Follows',
                                           title='Profile Visits vs. Follows')
fig_profile_visits_vs_follows.show()


# In[ ]:




