#Periodic Table, outputs data depending on which element is selected

print("Welcome!")

element = int(input("""

    Please select an element


    1 - Hydrogen
    2 - Lithium
    3 - Sodium
    4 - Fluorine
    5 - Chlorine
    6 - Bromine
   
    """))

if element == 1:
    print("""

    Name: Hydrogen
    Atomic Mass: 1
    Group: 1, Alkali

    """)

elif element == 2:
    print("""

    Name: Lithium
    Atomic Mass: 3
    Group: 1, Alkali

    """)

elif element == 3:
    print("""

    Name: Sodium
    Atomic Mass: 11
    Group: 1, Alkali

    """)

elif element == 4:
    print("""

    Name: Fluorine
    Atomic Mass: 9
    Group: 7, Halogens

    """)

elif element == 5:
    print("""

    Name: Chlorine
    Atomic Mass: 17
    Group: 7, Halogens

    """)

elif element == 6:
    print("""

    Name: Bromine
    Atomic Mass: 35
    Group: 7, Halogens

    """)

else:
    print("I'm afraid that isn't an option")