#!/usr/bin/env python3

# Input scenarios
# 1. input not a natural input of length such as -1
# 2. input not a numeric e.g hello


import sys

def unit_convert(length):
    '''
    convert length in meters to mm
    '''
    length = round(length *1000)

    return length

if __name__ == '__main__':
    input_args = sys.argv

    if len(input_args) == 2: # strictly two inputs
        try:
            input_length = input_args[1]
            length = float(input_length) # may raise value error if input not numeric

            if length < 0: # reject -1 values
                raise ValueError("Length cannot be negative")
            
            print(f"{unit_convert(length)} mm")
            sys.exit(0)
        except ValueError as e:
            print(f"'{input_length}' is an invalid value of length. Try again")
            print(f"{str(e)}")
            sys.exit(1)
    else:
        print("Invalid format: ")
        print("Usage: unit_converter.py <length_m>")
        sys.exit(1)