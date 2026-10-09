#!/usr/bin/env python3

import sys

print("-----------------------------------------------")
print(f"python version: {sys.version}")
print("-----------------------------------------------")

'''
Use: 
1. Calculate moments and reactions for simply suported beam
2. Compute data to plot BMD and SFD

'''


length = 10 # m 
udl_load = 10 # kN/m

def calculate_beam_response(length,udl_load):
    moment = round((udl_load*length*length)/8,2) # wl^2/8
    reaction = round((udl_load*length)/2,2)

    return moment, reaction


if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv)  == 2: # one or two inputs
        print("You did not enter values for length and udl load.")
        sys.exit(1)
    elif len(sys.argv) == 3: # two inputs only
        try:
            length = float(sys.argv[1])
            udl_load = float(sys.argv[2])
            if length <= 0 or udl_load <= 0:
                print("Invalid beam length or load.")
                sys.exit(1)
            moment, reaction = calculate_beam_response(length, udl_load)
            print(f"moment = {moment} kNm, reaction = {reaction} kN")
            sys.exit(0)
        except ValueError:
            print("Either length or udl load value is wrong format")
            sys.exit(1)
    else:
        print("Usage: simple_beam.py <length_m>  <udl_kN_per_m>")
        sys.exit(1)
    