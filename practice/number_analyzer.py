#!/usr/bin/python3
numbers = [12,7,18,3,15,10,21]
# numbers =[]

threshold = 10

def analyzer(numbers):
    if len(numbers):
        print(f"Numbers: {numbers}")
        print(f"Count: {len(numbers)}")
        print(f"Total: {sum(numbers)}")   
        print(f"Average: {round(sum(numbers)/len(numbers),2)}")   
        print(f"Minimum: {min(numbers)}")
        print(f"Maximum: {max(numbers)}")
        av = sum(numbers)/len(numbers)
        
        below_average = []
        above_average = []

        for number in numbers:
            if number > av:
                above_average.append(number)
            elif number < av:
                below_average.append(number)
            else:
                pass

        print("Below average:")      
        for item in below_average:
            print(item)

        print("Above average:")      
        for item in above_average:
            print(item)

analyzer(numbers)
