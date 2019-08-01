#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium
import pandas as pd


# In[2]:


national_parks_lat_long_csv = pd.read_csv('national_parks_lat_long.csv')
folium_map = folium.Map(location=[35.5236, -95.6750], zoom_start=4)
for index, row in national_parks_lat_long_csv.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']],
                        radius=10,
                        popup=row['Place Name'],
                       ).add_to(folium_map)

folium_map


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




