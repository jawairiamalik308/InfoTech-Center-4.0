# Programmer : JoJo Malik
# Date : 1.20.2023
# Program : InfoTechCenter Upgrades


"""
Our welcome screen will start our program letting  drivers know that the
info tech center 4.0 OS is loading
"""


# Import Libraies Here
import time
sleep = 2
print("\n\nWelcome - InfoTech Center 4.0\n")

import time
import sys

done = 'false'
#here is the animation
def animate():
    while done == 'false':
        sys.stdout.write('\Infotech center 4.0 is loading *')
        time.sleep(0.1)
        sys.stdout.write('\rInfotech center 4.0 is loading **')
        time.sleep(0.1)
        sys.stdout.write('\rInfotech center 4.0 is loading ***')
        time.sleep(0.1)
        sys.stdout.write('\rInfotech center 4.0 is loading ** ')
        time.sleep(0.1)
        sys.stdout.write('\rInfotech center 4.0 is loading *')
    sys.stdout.write('\rDone!     ')

animate()
#long process here
done = 'false'




