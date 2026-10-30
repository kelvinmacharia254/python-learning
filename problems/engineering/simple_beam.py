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
    """
    function to calculate midspan moment, support reactions,
    SFD and BMD for a simply supported beam
    """
    moment = (udl_load*length*length)/8 # wl^2/8
    reaction = (udl_load*length)/2 # wl/2

    x_values = [] # interval breaks
    moment_at_x = [] # moment values to plot BMD
    shear_at_x = [] # shear values to plot SFD

    intervals = 10 # selected number of intervals
    spacing = length/intervals # spacing
    
    for i in range(intervals+1):
         x = i*spacing # x value is given by i_th interval multiplied by interval spacing 
         x_values.append(x)
         moment_x = udl_load*x*((length/2)-(x/2))
         shear_x = udl_load*((length/2)-x)

         moment_at_x.append(moment_x)
         shear_at_x.append(shear_x)

    return moment, reaction, x_values , moment_at_x, shear_at_x


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
            moment, reaction, x_values, moment_at_x, shear_at_x = calculate_beam_response(length, udl_load)
            print(f"moment = {moment} kNm, reaction = {reaction} kN")

            print("x_values:")
            print(f"{x_values}")
            print("Moment at x:")
            print(f"{moment_at_x}")
            print("Shear at x:")
            print(f"{shear_at_x}")
            sys.exit(0)
        except ValueError:
            print("Either length or udl load value is wrong format")
            sys.exit(1)
    else:
        print("Usage: simple_beam.py <length_m>  <udl_kN_per_m>")
        sys.exit(1)
    
