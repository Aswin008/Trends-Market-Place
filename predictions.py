#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:06:01 2023

@author: aswin
"""

import json
import numpy as np
import urllib.request
import json
import os
import ssl
import datetime
from azure.eventhub import EventHubProducerClient, EventData
import random
import time

event_hub_namespace = "testhubevent"
event_hub_name = "newdemo"
sas_key_name = "policytest"
sas_key_value = "70KNK1XVlptpQ0eUUW5neKPFkCMBkDC42+AEhKdrTt8="

event_hub_connection_string = 'Endpoint=sb://testhubevent.servicebus.windows.net/;SharedAccessKeyName=policytest;SharedAccessKey=70KNK1XVlptpQ0eUUW5neKPFkCMBkDC42+AEhKdrTt8=;EntityPath=newdemo'

# Assuming you have a trained model (replace 'your_model' with your actual model)
# For demonstration, let's create a simple dummy model

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)

# Simulate real-time data arrival in a for loop
for _ in range(100):
    # Simulate a random input data point
    random_input_data = {
        "PageViews": np.random.randint(1, 50),
        "TimeSpentOnSite": np.random.uniform(10, 600),
        "ActionsPerformed": np.random.choice(['click', 'hover', 'scroll']),
        "Location": np.random.choice(['USA', 'Europe', 'Asia']),
        "DeviceType": np.random.choice(['Desktop', 'Mobile', 'Tablet']),
        "ReferralSource": np.random.choice(['Direct', 'Search', 'Social']),
        "DayOfWeek": np.random.randint(0, 6),  # Assuming 0 for Monday, 1 for Tuesday, and so on
        "TimeOfDay": np.random.randint(0, 24),
        "InteractedWithPromotion": np.random.choice([0, 1])
    }

    
    data =  {
      "input_data": {
        "data": [{
          "PageViews" : random_input_data['PageViews'],
          "TimeSpentOnSite" : random_input_data['TimeSpentOnSite'],
          "ActionsPerformed" : random_input_data['ActionsPerformed'],
          "Location" : random_input_data['Location'],
          "DeviceType" : random_input_data['DeviceType'],
          "ReferralSource" : random_input_data['ReferralSource'],
          "DayOfWeek": random_input_data['DayOfWeek'],
          "TimeOfDay" : random_input_data['TimeOfDay'],
          "InteractedWithPromotion" : 1
        }]
      }
    }
    

    body = str.encode(json.dumps(data))

    
    url = 'https://mlworkspace-tgdwv.eastus.inference.ml.azure.com/score'
    
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = '2cuoWFfsrf3HNtMLCAue6I9tgyDjotYd'
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")
    
    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'mlregression25-1' }
    
    req = urllib.request.Request(url, body, headers)
    
    user_score = 0
    try:
        response = urllib.request.urlopen(req)
    
        result = response.read()

        print(result)
        user_score = float(result.decode('utf-8')[1:-1])
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
    
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
        

    
    url_cl = 'https://mlworkspace-classification.eastus.inference.ml.azure.com/score'
    api_key_sl = '4FI9ll4dd1aa0e6zatElkpDMeWhgpYQe'
    
    if not api_key_sl:
        raise Exception("A key should be provided to invoke the endpoint")
    
    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key_sl), 'azureml-model-deployment': 'classificationj29-1' }
    
    req_cl= urllib.request.Request(url_cl, body, headers)
    
    pred_out = 0
    try:
        response = urllib.request.urlopen(req_cl)
    
        result = response.read()

    
        pred_out = int(result.decode('utf-8')[1:-1])
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
    
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
    

   

    # Convert the dictionary to a JSON string


    data["input_data"]["data"][0]["userEngagementScore"] = user_score
                
    data["input_data"]["data"][0]["potentialPurchase"] = pred_out
    
    producer = EventHubProducerClient.from_connection_string(conn_str=event_hub_connection_string, eventhub_name=event_hub_name)

    try:
        event_data_batch = producer.create_batch() 
        delay = random.uniform(0, 1)
        time.sleep(delay)
        
        event = {
         "PageViews" : data["input_data"]["data"][0]["PageViews"],
         "TimeSpentOnWebsite" : data["input_data"]["data"][0]["TimeSpentOnSite"],
         "ActionsPerformed": data["input_data"]["data"][0]["ActionsPerformed"],
         "Location": data["input_data"]["data"][0]["Location"],
         "DeviceType" : data["input_data"]["data"][0]["DeviceType"],
         "ReferralSource" :   data["input_data"]["data"][0]["ReferralSource"],
         "DayOfWeek": data["input_data"]["data"][0]["DayOfWeek"],
         "TimeOfDay": data["input_data"]["data"][0]["TimeOfDay"],
         "InteractedWithPromotion": data["input_data"]["data"][0]["InteractedWithPromotion"],
         "userEngagementScore": data["input_data"]["data"][0]["userEngagementScore"],
         "potentialPurchase": data["input_data"]["data"][0]["potentialPurchase"]  
         
     }
        s = json.dumps(event)
        print(s)
        
        event_data_batch.add(EventData(s)) # Add event data to the batch.
        producer.send_batch(event_data_batch)
    except KeyboardInterrupt:
        producer.close()

                
    # Print or use the generated JSON string
  
