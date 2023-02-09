# Programmer: Jawairia Malik
#Date: 2.8.2023
#Program: Weather System Updates

#Import Libraries Here
import random

# Create weather conditions in a list and choose it randomly

def weather():
  weatherForecast =   ["Snowing", "Blizzard", "Raining", "Sunny", "Partly Cloudy", "Sleet", "Tornado"]
  weatherCondition = random.choice(weatherForecast) 
  return weatherCondition 


#Variable to call weather() function once in our VRS() system(VRS is vehicle response system)
weatherAlert = weather() 

print(weatherAlert)

#VRS() to respond to the weather conditions

def v_r_s(): 
    print("Howdy")