#!/usr/bin/python3

# Instructions
# - Run from CLI

# Test cases
# python number_analyzer.py 14
# python number_analyzer.py hello
# python number_analyzer.py

import sys

numbers = [12,7,18,3,15,10,21]
# numbers =[]


def analyzer(numbers, threshold):
    """
    get a list of numbers and classify member as below or above average and also threshold provided via the CLI
    """
    if len(numbers): # list not empty
        print(f"Numbers: {numbers}")
        print(f"Count: {len(numbers)}")
        print(f"Total: {sum(numbers)}")   
        print(f"Minimum: {min(numbers)}")
        print(f"Maximum: {max(numbers)}")
        av = sum(numbers)/len(numbers)
        print("--------------------------")
        print(f"Threshold: {threshold}")    
        
        below_threshold = []
        above_threshold = []
        below_average = []
        above_average = []

        for number in numbers:
            if number > threshold:
                above_threshold.append(number)
            elif number < threshold:
                below_threshold.append(number)
            else:
                pass

            if number > av:
                above_average.append(number)
            elif number < av:
                below_average.append(number)
            else:
                pass

        print("Below Threshold:")      
        for item in below_threshold:
            print(item)

        print("Above Threshold:")      
        for item in above_threshold:
            print(item)

        print("---------------------------------------")
        print(f"Average: {round(av, 2)}")
        print("Below average:")      
        for item in below_average:
            print(item)
        
        print("Above average:")      
        for item in above_average:
            print(item)

if __name__ == '__main__':
    # analyzer(numbers)
    if len(sys.argv)>1: # Check if threshold is provide. Prevents IndexError
        try: # threshold to a valid integer
            threshold = int(sys.argv[1])
        except ValueError: 
            print(f"{sys.argv[1]} is not a Valid threshold. Integer required.")
            sys.exit()
    else:
        print("You did not provide a threshold in CLI args")
        sys.exit()

    analyzer(numbers, threshold)
        
