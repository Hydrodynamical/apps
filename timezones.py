#!/usr/bin/env python
# coding: utf-8

import datetime
import pytz
import time

def print_timezones():
    # Create a dictionary that maps city names to their time zone names
    city_timezones = {
        "Honolulu": "Pacific/Honolulu",
        "SF": "America/Los_Angeles",
        "Austin": "America/Chicago",
        "NYC": "America/New_York",
        "Paris": "Europe/Paris",
        "Bangkok": "Asia/Bangkok",
        "Shanghai": "Asia/Shanghai",
        "Tokyo": "Asia/Tokyo",
        "Sydney": "Australia/Sydney",
    }

    # Get the current time in GMT
    gmt = pytz.timezone("GMT")
    current_time_gmt = datetime.datetime.now(gmt)
    local_time = datetime.datetime.now(gmt)
    current_time_gmt_12hr = current_time_gmt.strftime("%I:%M %p")
    
    # Loop over the city time zones and print the current time for each city
    for city, timezone_name in city_timezones.items():
        timezone = pytz.timezone(timezone_name)
        current_time = current_time_gmt.astimezone(timezone)
        current_time_12hr = current_time.strftime("%I:%M %p")
        current_time_day = current_time.day
        current_time_month = current_time.month
        current_time_day_of_week = current_time.strftime("%A")
        print(f"{city:<10} {current_time_12hr:<10} {current_time_day_of_week:<10} {current_time_month}/{current_time_day}")
        print("---------------------------------------------")

print_timezones()




