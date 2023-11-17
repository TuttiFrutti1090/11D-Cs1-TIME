results = [1, 2, 4, 13, 22, 31, 41, 54, 67, 80]

def grade(score):
    if score >= results[0]:
        print('U')
    elif score <= results[1] and score > results[0]:
        print(1)
    elif score <= results[2] and score > results[1]:
        print(2)
    elif score <= results[3] and score > results[2]:
        print(3)
    elif score <= results[4] and score > results[3]:
        print(4)
    elif score <= results[5] and score > results[4]:
        print(5)
    elif score <= results[6] and score > results[5]:
        print(6)
    elif score <= results[7] and score > results[6]:
        print(7)
    elif score <= results[8] and score > results[7]:
        print(8)
    elif score <= results[9] and score > results[8]:
        print(9)
