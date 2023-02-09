# Programmer: Jawairia Malik
#Date: 2.8.2023
#Program: Weather System Updates

#Import Libraries Here
import random

# Create weather conditions in a list and choose it randomly

def weather():
  weatherForecast =   ["Heavy Snow", "Blizzard", "Rain", "Sunny", "Partly Cloudy", "Sleet", "Tornado"]
  weatherCondition = random.choice(weatherForecast) 
  return weatherCondition 


#Variable to call weather() function once in our VRS() system(VRS is vehicle response system)
weatherAlert = weather() 

weatherAlert = "Heavy Snow"


#VRS() to respond to the weather conditions

def v_r_s(): 
  if weatherAlert == "Heavy Snow":
    print("\nNWS has changed your alarm by 15 minutes due to", weatherAlert)
    print("\nYour VRS has been engaged only allowing your vehicle to go 45 MPH")


print(v_r_s())
