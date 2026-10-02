#!/usr/bin/env python3

# Instruction
# - Run from CLI
# - Test cases
# $ python value_summary.py 12 7 18 3
# $ python value_summary.py
# $ python value_summary.py 12 hello 18

import sys

number_list = [1,2,3] # Test input


def summary(lst):
    if len(lst): # list not empty
        total = sum(lst) # calculate total
        average = total/len(lst) # average
        print(f"Total: {total}")
        print(f"Average: {average}")
        for number in lst:
            if number > average:
                print(f"{number} is above the average")
            elif  number < average:
                print(f"{number} is below the average")
            else:
                print(f"{number} is  equal to the average")
    else:
        print("The number list is empty")

# self test
if __name__ == "__main__":
    number_list = []
    for n in sys.argv[1:]: # slice list to remove [0] i.e script name
        try:
            number = int(n)
            number_list.append(number)
        except ValueError:
            print("One or more args in not a valid int.")
            sys.exit()

    print(number_list)
    summary(number_list)



    
    