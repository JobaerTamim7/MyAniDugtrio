# This cell is for import part

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import json


# This cell is for const purpose

# In[2]:


url = 'https://myanimelist.net/topanime.php'  


# Headless chrome setup

# In[6]:


options = webdriver.ChromeOptions()
options.add_argument('headless=new')

driver = webdriver.Chrome(options=options)
driver.get(url)


# Scraping web data

# In[7]:


try:
    rank_data = WebDriverWait(driver,5).until(
        expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,'table.top-ranking-table tr.ranking-list'))
    )[:10]
    obj_list = []
    for data in rank_data:
        rank = data.find_element(By.CSS_SELECTOR,'td.rank').text
        title = data.find_element(By.CSS_SELECTOR,'td.title h3').text
        img_link = data.find_element(By.CSS_SELECTOR,'td.title a img').get_attribute('src')
        anime_dict = {
            "rank" : rank,
            "title" : title,
            "img_link" : img_link
        }
        obj_list.append(anime_dict)
finally:
    driver.quit()


# JSON Time !!!!!!!

# In[8]:


with open('all_top_anime.json','w') as file:
    json.dump(obj_list,file,indent=4)

print('200 Sucess!')

