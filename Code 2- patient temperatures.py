#!/usr/bin/env python
# coding: utf-8

# In[12]:


# input temperature
temperature = input("Enter the patient's temperature (in degrees Fahrenheit): ")


# In[13]:


#check temperature
if temperature.replace(".","",1).isdigit(): 
    temperature_input = float(temperature)
    
    if temperature_input >= 99.5:
        print("The patient has a high temperature.")
    else:
        print("The patient has a normal temperature")
else:
    print("Error: Please enter a valid temperature (numeric value).")
    
        


# In[ ]:




