#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:30:06 2023

@author: aswin
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta




# Simulate historical clickstream data, to train the models
def simulate_clickstream_data(num_samples=10000):
    data = []

    for _ in range(num_samples):
        # Simulate features 
        page_views = np.random.randint(1, 50)
        time_spent_on_site = np.random.uniform(10, 600)
        actions_performed = random.choice(['click', 'hover', 'scroll'])
        
        # Simulate additional features
        location = random.choice(['USA', 'Europe', 'Asia'])
        device_type = random.choice(['Desktop', 'Mobile', 'Tablet'])
        referral_source = random.choice(['Direct', 'Search', 'Social'])

        # Simulate time-related features
        current_time = datetime.now()
        day_of_week = current_time.weekday()
        time_of_day = current_time.hour

        # Simulate promotion interaction
        interacted_with_promotion = np.random.choice([0, 1], p=[0.9, 0.1])

        # Total score of each user is calculated based upon various matrix
        action_score  = 0
        
        if actions_performed == 'click':
            action_score = 200
        elif actions_performed == 'hover':
            action_score = 100
        else:
            action_score = 50
        
        device_score = 0
        
        if device_type == 'Desktop':
            device_score = 100
        elif device_type == 'Tablet':
            device_score = 50
        else:
            device_score = 20
       
        refer_score = 0
        if referral_source == 'Search':
            refer_score = 250
        elif referral_source == 'Direct':
            refer_score = 175
        else:
            refer_score = 120
        
        promo_score = -10
        
        score = (0.1 * page_views + 0.4 * time_spent_on_site + 0.2 * action_score \
            + 0.05 * device_score +  0.15 * refer_score + 0.1 * promo_score)
        
        tot_score = 0.1 * 50 + 0.4 * 600 + 0.2 * 200 + 0.05 * 100 + 0.15 * 250
        
        pp = score / (tot_score + 400)
        
        op = 1 - pp
        


        # If a person would purchase or not in real world is a random choice but with greater probability if they are active using the app
        is_converted = np.random.choice([0, 1], p=[op, pp])


        # User engagement score as a function of score and if a person purchased a product or not
        user_engagement_score = is_converted * 300 + score
   

        data.append([
            page_views, time_spent_on_site, actions_performed,
            location, device_type, referral_source,
            day_of_week, time_of_day, interacted_with_promotion, is_converted,
            user_engagement_score
        ])

    columns = [
        'PageViews', 'TimeSpentOnSite', 'ActionsPerformed',
        'Location', 'DeviceType', 'ReferralSource',
        'DayOfWeek', 'TimeOfDay', 'InteractedWithPromotion', 'IsConverted',
        'UserEngagementScore'
    ]
    df = pd.DataFrame(data, columns=columns)
    return df

# Generate simulated clickstream data
clickstream_data = simulate_clickstream_data(num_samples=5000)

# Display the first few rows of the dataset
print(clickstream_data.head())

# Save the dataset as a CSV file
clickstream_data.to_csv('simulated_clickstream_data_updated_v2.csv', index=False)
