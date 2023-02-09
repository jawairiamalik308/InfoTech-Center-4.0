#Merged Welcome and Gasoline branches  - stable
#Programer: Jawairia Malik
#Date merged: 2.6.2023

"""
Our welcome screen will start our program letting  drivers know that the
info tech center 4.0 OS is loading
"""


# Import Libraies Here
import random
from time import sleep
import time


import time
import sys

done = 'false'
# Import any Libraries Here
import time  # I imported the time library for further use in code.
import sys  # I imported the system library for further use in code.

print('\n\033[1;34;48m Welcome to Infotech Center 4.0')

x = 0
a = 0

time.sleep(2)
print('')

while x != 20:
    x += 1
    b = ("\033[1;33;40m Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;40m Done!')










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
        print("\n***WARNING, GAS IS EMPTY***")
        sleep(1)
        print("Calling Emergency Contact...")
    elif gas_level_indicator == "Low":
        print("\n***WARNING, GAS IS LOW***")
        sleep(1)
        print("\nSearching for nearest gas station...")
        sleep(2)
        print("\nNearest gas station is",list_of_gas_stations(),",",miles_to_gas_station_low,"miles away")
    elif gas_level_indicator == "Quarter tank":
        print("\nYou have quarter tank")
        sleep(1)
        print("\nSearching for nearest gas station...")
        sleep(2)
        print("\nNearest gas station is",list_of_gas_stations(),",",miles_to_gas_station_quarter,"miles away" )
    elif gas_level_indicator == "Half tank":
        print("\nHalf tank, good level of gas.")
    elif gas_level_indicator == "Three Quarter tank":
        print("\nYour gas levels are good. You have three quarters of a tank.")
    else:
        print("\nYour gas is full.")

gas_level_alert()





