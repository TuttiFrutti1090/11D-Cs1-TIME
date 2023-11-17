# Program to roll a die, outputting an ASCII and UNICODE representation of the die face

import random
# Needed for the die to roll

# Dictionary to look-up the face for each number
die_faces = {1:"""
              _______
             |       |
             |   ○   |
             |       |
              ¯¯¯¯¯¯¯
             """,
             2:"""
              _______
             | ○     |
             |       |
             |     ○ |
              ¯¯¯¯¯¯¯
             """,
             3:"""
              _______
             | ○     |
             |   ○   |
             |     ○ |
              ¯¯¯¯¯¯¯
             """,
             4:"""
              _______
             | ○   ○ |
             |       |
             | ○   ○ |
              ¯¯¯¯¯¯¯
             """,
             5:"""
              _______
             | ○   ○ |
             |   ○   |
             | ○   ○ |
              ¯¯¯¯¯¯¯
             """,
             6:""""
              _______
             | ○   ○ |
             | ○   ○ |
             | ○   ○ |
              ¯¯¯¯¯¯¯
             """
             }

def roll_die():
    # 'Rolls' the die, returning an integer
    result = random.randint(1,6)
    
    # Looks up the corresponding face
    result_face = die_faces[result]
    
    return result_face

# Rolls the die and prints the output face
print(roll_die())

while __name__ == "__main__":
    choice = input("How many times would you like to roll the die? (0 to exit)")
    
    # Exits the program if the user inputs "0"
    if choice == "0":
        break
    
    try:
        # Converts the string input to integer
        count = int(choice)
        
        if count < 0:
            # Asks for the input again if not positive
            print("Please enter a valid integer.")
            pass
        
        # Initialises an array for the results to be placed in
        results = []
        
        # Rolls the die for the specified amount of times, and appends it to the results array
        for i in range(count):
            results.append(roll_die())
        
        # Prints out the results, separated on different lines
        print("\n".join(results))
    except:
        
        # Asks for the input again if not an integer
        print("Please enter a valid integer.")
        pass
    