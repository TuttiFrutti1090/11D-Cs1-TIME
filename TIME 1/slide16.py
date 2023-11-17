# Carpet cost calculator

import math
# Used to calculate the gripper cost

import re
# Used to parse input


def calculate_cost(width, length, unit_price):
    
    # Calculates the cost of each parameter
    underlay_cost = width * length * 3
    carpet_cost = width * length * unit_price
    gripper_cost = math.ceil(width * 2 + length * 2)
    fitting_fee = 50
    
    # Finds the total cost and returns it with a "£"
    # Also check if total is an integer
    cost = underlay_cost + carpet_cost + gripper_cost + fitting_fee
    if cost % 1 != 0:
        cost = math.ceil(cost*100)/100
        return f"£{cost}"
    else:
        return f"£{int(cost)}"
while __name__ == "__main__":
    
    # Ask the user for the information about the room and carpet
    info = input("Please enter the dimensions of the room in metres, and the unit price in £/m^2. (WIDTH x LENGTH @ UNITPRICE)")
    
    try:
        # Parses the input, getting the unit price and dimensions of the room, and makes the unit price positive
        unit_price = abs(float(re.split("@", info.strip())[-1]))
        dimensions = re.split("@", info.strip())[0]
        width, length = re.split("x", dimensions)
        
        # Checks that the dimensions are numbers, and makes them positive if negative
        width = abs(float(width))
        length = abs(float(length))
        
        # Calculates the cost and prints it out
        cost = calculate_cost(width=width, length=length, unit_price=unit_price)
        print(cost)
    except:
        print("Please enter valid information in the correct format (WIDTH x LENGTH x UNIT_PRICE)")
        pass