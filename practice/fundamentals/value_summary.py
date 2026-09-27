#!/usr/bin/env python3

import sys

number_list = [1,2,3] # Test input


def summary(lst):
    if len(lst):
        total = sum(lst)
        average = total/len(lst)
        print(f"Number list: {lst}")
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
    if len(sys.argv) > 1:
        print(f"sys.argv: {sys.argv[0]}, {sys.argv[1]}")
    summary(number_list)