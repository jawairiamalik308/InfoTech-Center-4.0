
# Programmer : JoJo Malik
# Date : 1.30.2023
# Program : InfoTechCenter Gasoline

"""
We will make a Function that will tell us our fuel gauge level
    -Make a list with Gas Levels
    -Randomize the list to determine our gas level

Create a Function to determine our closest gas station
    -list of gas stations
    -randomize and choose from list, a gas stations

Create a Function to determine our gas level and closest gas station
    -print gas level
    -print closest gas station
"""
import time

#Gas level Function

def gas_level_gauge():

    gas_level_list = ["Empty","Low","Quarter tank","Half tank","Three Quarter tank","Full"]
    current_gas_level = random.choice (gas_level_list)
    return current_gas_level

    gas_level_indicator = gas_level_gauge()


#List of gas stations function


def list_of_gas_stations():
    gas_stations = ["Shell","Speedway","Costco","Sams Club","Circle K","Meijer","Marathon"]
    gas_station_nearby = random.choice (gas_stations)
    return gas_station_nearby




# Determine gas level and closest gas station

def gas_level_alert():
    miles_to_gas_station_low = round(random.uniform(1, 25), 2)
    miles_to_gas_station_quarter = round(random.uniform(26, 50), 2)
    if gas_level_indicator == "Empty":
        print("\n***WARNING, GAS IS EMPTY***")
        time.sleep(1)
        print("Calling Emergency Contact...")
    elif gas_level_indicator == "Low":
        print("\n***WARNING, GAS IS LOW***")
        time.sleep(1)
        print("\nSearching for nearest gas station...")
        time.sleep(2)
        print("\nNearest gas station is",list_of_gas_stations(),",",miles_to_gas_station_low,"miles away")
    elif gas_level_indicator == "Quarter tank":
        print("\nYou have quarter tank")
        time.sleep(1)
        print("\nSearching for nearest gas station...")
        time.sleep(2)
        print("\nNearest gas station is",list_of_gas_stations(),",",miles_to_gas_station_quarter,"miles away" )
    elif gas_level_indicator == "Half tank":
        print("\nHalf tank, good level of gas.")
    elif gas_level_indicator == "Three Quarter tank":
        print("\nYour gas levels are good. You have three quarters of a tank.")
    else:
        print("\nYour gas is full.")



















import random

# Import Libraries here


# Programmer: Jawairia Malik
#Date: 2.8.2023
#Program: Weather System Updates



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
    print("\nYour VRS has been engaged only allowing your vehicle to go 45 MPH")
  elif weatherAlert == "Blizzard":
    print("\nNWS has changed your alarm by 45 minutes due to", weatherAlert)
    print("\nVRS has been engaged only allowing your car to go 20 MPH")
  elif weatherAlert == "Raining":
    print("\nIt is", weatherAlert)
    print("\nBring an umbrella today")
  elif weatherAlert == "Sunny":
    print("\nIt is", weatherAlert)
    print("\nAir quality is good today.")
  elif weatherAlert == "Partly Cloudy":
    print("\nIt is", weatherAlert)
  elif weatherAlert == "Sleet":
    print("\nNWS has changed your alarm by 30 minutes due to", weatherAlert)
    print("\nVRS has been engaged only allowing your car to go 20 MPH")
  else:
    print("\nNWS has changed your alarm by one hour due to", weatherAlert)
    print("\nTake shelter")


# temp

def weatherTemp():
    tempHot = round(random.uniform(50, 100))
    tempCold = round(random.uniform(10, 40))
    if weather == "Heavy Snow":
        print("\nIt is",tempCold,"degrees outside")
        print("Your heat has turned ON")
    elif weather == "Blizzard":
        print("\nIt is",tempCold,"degrees outside")
        print("Your heat has turned ON")
    elif weather == "Raining":
        print("\nIt is",tempCold,"degrees outside")
    elif weather == "Sunny":
        print("\nIt is",tempHot,"degrees outside")
        print("Your AC is turned ON")
    elif weather == "Partly Cloudy":
        print("\nIt is",tempHot,"degrees outside")
        print("Your AC has been turned ON")
    elif weather == "Sleet":
        print("\nIt is",tempCold,"degrees outside")
        print("Your heat has been turned ON")
    else:
        print("\nIt is",tempHot,"degrees outside")

weatherTemp()








# Call Functions Here
v_r_s()

weatherTemp()