#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install openai==0.28.0 selenium webdriver-manager')
get_ipython().system('apt-get update')
get_ipython().system('apt-get install -y chromium-chromedriver')
get_ipython().system('cp /usr/lib/chromium-browser/chromedriver /usr/bin')


# In[ ]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import openai

# Set up OpenAI API key
openai.api_key = ''

# Set up Chrome options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize WebDriver using webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open the form
driver.get('https://form.jotform.com/241617189501153')

# Allow the page to load
time.sleep(1)

# Function to generate dummy data
def generate_dummy_data(prompt, max_tokens=10):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return response.choices[0].message['content'].strip()


# Fill out the form fields
fields = {
    "First Name": generate_dummy_data("Generate a random male first name."),
    "Middle Name": generate_dummy_data("Generate a random middle name."),
    "Last Name": generate_dummy_data("Generate a random last name."),
    "Street Address": generate_dummy_data("Generate a random street address."),
    "Street Address Line 2": generate_dummy_data("Generate a random street address line 2."),
    "City": generate_dummy_data("Generate a random city."),
    "State": generate_dummy_data("Generate a random state."),
    "Postal/Zip Code": generate_dummy_data("Generate a random postal/zip code."),
    "Email": generate_dummy_data("Generate a random email id."),
    "Phone Number": generate_dummy_data("Generate a random Indian phone number."),
    "LinkedIn": generate_dummy_data("Generate a LinkedIn URL."),
    "Interesting AI/LLMs": generate_dummy_data("Write something interesting about AI agents/LLMs.", max_tokens=50),
    "Interesting Web Automation": generate_dummy_data("Write something interesting about web automation.", max_tokens=50),
    "Reverse Linked List": generate_dummy_data("Provide code to reverse a linked list in Python.", max_tokens=50),
    "Resume": 'C:\\Users\\Venkata Raghava\\OneDrive\\Documents\\Rajesh\\Rajesh_Resume.pdf',  # Update this with the path to your resume
    "Cover Letter": generate_dummy_data("Write a short cover letter.", max_tokens=50)
}


# Initialize WebDriverWait
wait = WebDriverWait(driver, 20)

# Fill text fields with explicit waits
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first_11"]'))).send_keys(fields["First Name"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="middle_11"]'))).send_keys(fields["Middle Name"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="last_11"]'))).send_keys(fields["Last Name"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_16_addr_line1"]'))).send_keys(fields["Street Address"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_16_addr_line2"]'))).send_keys(fields["Street Address Line 2"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_16_city"]'))).send_keys(fields["City"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_16_state"]'))).send_keys(fields["State"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_16_postal"]'))).send_keys(fields["Postal/Zip Code"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_12"]'))).send_keys(fields["Email"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_13_full"]'))).send_keys(fields["Phone Number"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_19"]'))).send_keys(fields["LinkedIn"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_24"]'))).send_keys(fields["Interesting AI/LLMs"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_25"]'))).send_keys(fields["Interesting Web Automation"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_23"]'))).send_keys(fields["Reverse Linked List"])
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_22"]'))).send_keys(fields["Cover Letter"])
time.sleep(2)
# Upload Resume
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_17"]'))).send_keys(fields["Resume"])
time.sleep(1)

# Submit the form
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_9"]'))).click()

# Close the driver after some time
time.sleep(5)
driver.quit()


# In[ ]:




