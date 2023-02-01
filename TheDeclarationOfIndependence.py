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


# Import Libraries here
import random
from time import sleep
# Gas level Function

def gas_level_gauge():
    gas_level_list = ["Empty","Low","Quarter tank","Half tank","Three Quarter tank","Full"]
    current_gas_level = random.choice (gas_level_list)
    return current_gas_level

#Variable calling gas level gauge function to store its value
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
        print("***WARNING, GAS IS EMPTY***")
        sleep(1)
        print("Calling Emergency Contact...")
    elif gas_level_indicator == "Low":
        print("***WARNING, GAS IS LOW***")
        sleep(1)
        print("Checking Google Maps for nearest gas station...")
        sleep(2)
        print("Nearest gas station is",list_of_gas_stations(),",",miles_to_gas_station_low,"miles away")

gas_level_alert()




