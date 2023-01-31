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


# Gas level Function

def gas_level_gauge():
    gas_level_list = ["Empty","Low","Quarter","Half","Three Quarter","Full"]
    current_gas_level = random.choice (gas_level_list)
    return current_gas_level

print(gas_level_gauge())



def list_of_gas_stations(): 
    gas_stations = ["Shell","Speedway","Costco","Sams Club","Circle K","Meijer","Marathon"]
    gas_station_nearby = random.choice (gas_stations)
    print("Your nearest gas station is",gas_station_nearby,".")
    return gas_station_nearby






