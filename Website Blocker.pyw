#!/usr/bin/env python
# coding: utf-8

# In[36]:


import time
from datetime import datetime as dt

hosts_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
host_temp = 'hosts'
website_list = ['facebook.com','www.facebook.com']

#while True:
for i in range(2):
    if dt(dt.now().year,dt.now().month,dt.now().day,16) < dt(dt.now().year,dt.now().month,dt.now().day,21):
        with open(hosts_path,'r+') as file:
            content = file.read()
            for i in website_list:
                if i in content:
                    pass
                else:
                    file.write(redirect+' '+i+'\n')
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        time.sleep(5)


# In[ ]:




