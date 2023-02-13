# Programmer: Jawairia Malik
#Date: 2.8.2023
#Program: Weather System Updates

#Import Libraries Here
import random

# Create weather conditions in a list and choose it randomly

def weather():
  weatherForecast =   ["Heavy Snow", "Blizzard", "Raining", "Sunny", "Partly Cloudy", "Sleet", "Tornado"]
  weatherCondition = random.choice(weatherForecast) 
  return weatherCondition 


#Variable to call weather() function once in our VRS() system(VRS is vehicle response system)
weatherAlert = weather() 




#VRS() to respond to the weather conditions

def v_r_s(): 
  if weatherAlert == "Heavy Snow":
    print("\nNWS has changed your alarm by 15 minutes due to", weatherAlert)
    print("Your VRS has been engaged only allowing your vehicle to go 45 MPH")
  elif weatherAlert == "Blizzard":
    print("\nNWS has changed your alarm by 45 minutes due to", weatherAlert)
    print("VRS has been engaged only allowing your car to go 20 MPH")
  elif weatherAlert == "Raining":
    print("\nIt is", weatherAlert)
    print("Bring an umbrella today")
  elif weatherAlert == "Sunny":
    print("\nIt is", weatherAlert)
    print("Air quality is good today.")
  elif weatherAlert == "Partly Cloudy":
    print("\nIt is", weatherAlert)
  elif weatherAlert == "Sleet":
    print("\nNWS has changed your alarm by 30 minutes due to", weatherAlert)
    print("VRS has been engaged only allowing your car to go 20 MPH")
  else:
    print("\nNWS has changed your alarm by one hour due to", weatherAlert)
    print("Take shelter")

v_r_s()








