"""
BEAM LOAD CALCULATOR
--------------------
Use: Calculate support reactions for as simply supported beam with any number of point loads

"""

import math


test_cases = [
    (8.0, [(20, 2), (35, 4), (15, 6)], 36.25, 33.75), # (span, loads, expected_ra, expected_rb)
    (20.0, [(60, 5), (70, 10), (80, 15)], 100.0, 110.0),
    (8.0, [(40, 2)], 30.0, 10.0),
]

def calculate_reactions(span, loads):
    """

    """
    reaction_a = 0
    reaction_b = 0
    total_load = 0
    applied_moment_a = 0

    for magnitude, position in loads:
        # utilize influence lines ordinate to compute reactions
        ordinate1 = (span - position )/span # ordinate from left support
        ordinate2 = position /span # ordinated from right support
        # super imposed reaction and moments / accumilate reaction & at each support
        reaction_a += ordinate1*magnitude
        reaction_b += ordinate2*magnitude
        total_load += magnitude
        applied_moment_a += magnitude*position

    # equibrium checks
    moment_check = applied_moment_a - (reaction_b* span) # take moment about a or another convinient location
    total_load_check = reaction_a +reaction_b - total_load

    equilibrium_check = (math.isclose(total_load_check, 0.00, abs_tol=1e-9) and math.isclose(moment_check , 0.00, abs_tol=1e-9))

    return reaction_a, reaction_b, total_load, applied_moment_a, equilibrium_check

# Test Load cases
test_pass_counter = 0
test_case_no = 0
test_case_bools = []
for span, load_case, expected_r_a, expected_r_b in test_cases:
    reaction_a, reaction_b, total_load, moment_a, equilibrium_check = calculate_reactions(span, load_case)
    # test
    reaction_a_test = math.isclose(reaction_a,expected_r_a, abs_tol=1e-9)
    reaction_b_test = math.isclose(reaction_b,expected_r_b, abs_tol=1e-9)
    overall_test_pass = equilibrium_check and reaction_a_test and reaction_b_test
    test_pass_counter += 1 if overall_test_pass else 0
    test_case_no += 1
    test_case_bools.append((test_case_no, overall_test_pass))
 
    # alternative approach to count test passed
    # if overall_test_pass:
    #     test_pass_counter += 1
        
    print(f"Span:{span:.2f}")
    print(f"Number of point loads:{len(load_case)}")
    print(f"Total load:{total_load:.2f}")
    print(f"Calculated R_A:{reaction_a:.2f}; Expected R_A: {expected_r_a}; {'Ok!' if reaction_a_test else 'Not ok!'}")
    print(f"Calculated R_B:{reaction_b:.2f}; Expected R_B: {expected_r_b}; {'Ok!' if reaction_b_test else 'Not ok!'}")
    print(f"Moment_A:{moment_a:.2f}")
    print(f"Equilibrium Check:{'PASS' if equilibrium_check else 'FAIL'}")
    print("-------------------------------------------------------------------------")


for test_case_no, test_result in test_case_bools:
    print(f"Test Case {test_case_no}:{'PASS' if test_result else 'FAIL'}")
print()
print(f"Tests passed: {test_pass_counter}/{len(test_cases)}") 
print(f"Overal suite: {'FAIL' if test_pass_counter != len(test_cases) else 'PASS'}")