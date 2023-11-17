#Energy bill calculator Problem:
# Outputs the raw cost of energy usage
def rawcost(prev, curr):
    unitsUsed = curr - prev
    calori3 = 39.3 / 3.6
    kWh = unitsUsed * 1.022 
    kWh = kWh * calori3
    return kWh * 2.84

# Circle properties problem:
# Returns the: radius, area, circumference and arc length of a circle
def properties(diameter, arcAngle):
    radius = diameter / 2
    radius2 = radius ** 2
    area = 3.14 * radius2
    circumference = 3.14 * diameter
    arcLength = circumference * arcAngle
    return radius, area, circumference, arcLength
