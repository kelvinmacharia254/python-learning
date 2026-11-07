"""
BEAM LOAD CALCULATOR
--------------------
Span: 8.0 m
Number of point loads: 3

Total load: 70.00 kN
Reaction A: 36.25 kN
Reaction B: 33.75 kN

Equilibium check: PASS
"""

import math

span = 8.0

loads = [
    (20, 2),
    (35, 4),
    (15, 6),
]

def calculate_reactions(span, loads):
    reaction_a = 0
    reaction_b = 0
    total_load = 0
    moment_a = 0

    for magnitude, position in loads:
        ordinate1 = (span - position )/span
        ordinate2 = position /span
        reaction_a += ordinate1*magnitude
        reaction_b += ordinate2*magnitude
        total_load += magnitude
        moment_a += magnitude*position

    moment_a = moment_a - (reaction_b* span)
    force_residual = reaction_a +reaction_b - total_load

    equilibrium_check = (math.isclose(force_residual, 0.00, abs_tol=1e-9) and math.isclose(moment_a, 0.00, abs_tol=1e-9))



    return reaction_a, reaction_b, total_load, moment_a, equilibrium_check

reaction_a, reaction_b, total_load, moment_a, equilibrium_check = calculate_reactions(span, loads)

print(f"Span:{span:.2f}")
print(f"Number of point loads:{len(loads)}")
print(f"R_A:{reaction_a:.2f}")
print(f"R_B:{reaction_b:.2f}")
print(f"Moment_A:{moment_a:.2f}")
print(f"Equilibrium Check:{'PASS' if equilibrium_check else 'FAIL'}")

