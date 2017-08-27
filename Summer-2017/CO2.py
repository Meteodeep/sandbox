#Algorithim/Function with 3 Constants
from time import sleep

currentCO2 = 404.77

currentyearlyincrease = 2.035

yearbyyearincrease = 0.036

while True:

        currentCO2 = currentCO2 + currentyearlyincrease + yearbyyearincrease
        print(currentCO2)
        yearbyyearincrease = yearbyyearincrease + 0.036
        sleep(5)


#Data: Climate Central/NOAA
#Calculated using Averages on Python 3
#Exponential Increase year-by-year
