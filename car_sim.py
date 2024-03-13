##
# Brady Bell and William Nichols
# Project 2
# Using Fuction definitions to calculate and show the miles traveled and other various factors of a car's trip.
##

import math

total_distance = 0
net_miles = 0

def find_max_distance(tank_size: float, mpg: float) -> float:
    max_distance = round(tank_size * mpg, 2)
    return max_distance


def go_forward(miles_forward) -> float:
    while total_distance < miles_forward:
        total_distance += 1
    net_miles = net_miles + miles_forward
    return net_miles

def do_choice1(max_distance) -> None:
    miles_forward = int(input("Distance Forward: "))
    if miles_forward < 0:
        print("cant drive negative miles")
        return
    net_distance = miles_forward + total_distance
    if net_distance > max_distance:
        too_far = net_distance - max_distance 
        print("Not Enough Fuel!")
        print(too_far, "miles too far!")
        user_loop(max_distance)
    else:
        total_distance = net_distance
        go_forward(miles_forward)

def go_back(miles_back) -> float:
    while total_distance < miles_back:
        total_distance += 1
    net_miles = net_miles - miles_back
    return net_miles

def do_choice2(max_distance) -> None:
    miles_back = int(input("Distance Back: "))
    if miles_back < 0:
        print("cant drive negative miles")
        return
    net_distance = miles_back + total_distance 
    if net_distance > max_distance:
        too_far = net_distance - max_distance 
        print("Not Enough Fuel!")
        print(too_far, "miles too far!")
        user_loop(max_distance)
    else:
        total_distance = total_distance + miles_back
        go_back(miles_back)

def user_loop(max_distance) -> int:
    loop = int(input("Enter 0-Calculate, 1-Forward, 2-Back: "))
    if loop == 0:
        loop = 0
        return  loop
    elif loop == 1:
        do_choice1(max_distance)
    elif loop == 2: 
        do_choice2(max_distance)
    else:
        user_loop(max_distance)

def find_gallon(mpg: float) -> float:
    try:
        gallons = round(total_distance / mpg, 2)
    except:
        print("MPG is zero!")
        gallons = 0
    return gallons

def total_cost(gallons: float, cost_gallon: float) -> float:
    cost = round(gallons * cost_gallon, 2)
    return cost

def report_stats(cost: float, gallons: float) -> str:
    if cost < 25.00:
        cost_str = "Cha Chiiinng!"
    elif cost < 100.00:
        cost_str = "Wallet getting nervous!"
    else:
        cost_str = "Ouch!"
    report_str = ("Total Miles Traveled: " +  str(total_distance) + "\n" + "Net Miles: " + 
 str(net_miles) + "\n" + "Gallons used: " + str(gallons) + "\n\n" + "Total Cost: $" + str(cost) + "\n" + str(cost_str))
    return report_str



        

def travel(tank_size, mpg, cost_gallon) -> str:
    max_distance = find_max_distance(tank_size, mpg)
    loop = 1
    while max_distance >= total_distance and loop != 0:
        loop = user_loop(max_distance)
    gallons = find_gallon(mpg)
    cost = total_cost(gallons, cost_gallon)
    report = report_stats(cost, gallons)
    return report


