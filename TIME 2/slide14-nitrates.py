# Calculates the dose for fish tank

def Dose(nitrate):
    if nitrate > 10:
        return 3
    elif nitrate > 2.5:
        return 2
    elif nitrate > 1:
        return 1
    else:
        return 0.5
while __name__ == "__main__":
    nitrate = input("What is the nitrate level?")
    try:
        nitrate = float(nitrate)
        print(f"For {nitrate} nitrate dose {Dose(nitrate)}ml")
    except:
        print("Please enter a valid number.")
        pass