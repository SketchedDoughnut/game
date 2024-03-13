##
# Brady Bell and William Nichols
# Project 2
# Using Fuction definitions to calculate and show the miles traveled and other various factors of a car's trip.
##

import car_sim

def main() -> None:
    tank_size = float(input("Tank size (gallons): "))
    mpg = float(input("MPG: "))
    cost_gallon = float(input("Cost per gallon: "))
    if tank_size < 0 or mpg < 0 or cost_gallon < 0:
        print("these values cannot be negative please enter them again")
        main()
    print(car_sim.travel(tank_size, mpg, cost_gallon))
main()