# Calculates the number of balls which will fit in a ball pit

import math
# Needed for Pi


# Calculates Ball Volume with formula 4/3πr^3
def ball_volume(r):
    volume = ( 4 / 3 ) * math.pi * r**3
    return volume

# Calculates Ball Pit Volume with formula πr^2h
def pit_volume(r, h):
    volume = math.pi * r**2 * h
    return volume

# Calculates how many balls could fit in a given pit with the formula (pd/bd)x0.75
def capacity(ball, pit):
    capacity = ( pit / ball ) * 0.75
    return capacity

# Requested case:
ball_volume = ball_volume(r=0.05)
pit_volume = pit_volume(r=1, h=0.2)
capacity = capacity(ball=ball_volume,pit=pit_volume)
print(capacity)