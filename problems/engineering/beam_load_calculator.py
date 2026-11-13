
"""
BEAM LOAD CALCULATOR
--------------------
Calculate support reactions for a simply supported beam
subjected to any number of vertical point loads.

Units:
    Span and positions: metres (m)
    Loads and reactions: kilonewtons (kN)
    Moments: kilonewton-metres (kNm)
"""

import math


# Test cases:
# (span, loads, expected_ra, expected_rb, expected_error)

test_cases = [
    (8.0, [(20, 2), (35, 4), (15, 6)], 36.25, 33.75, False),
    (20.0, [(60, 5), (70, 10), (80, 15)], 100.0, 110.0, False),
    (8.0, [(40, 2)], 30.0, 10.0, False),
    (8.0, [], 0.0, 0.0, False),

    # Invalid spans — ValueError expected
    (0, [], None, None, True),
    (-8.0, [(40, 2)], None, None, True),
]


def calculate_reactions(span, loads):
    """
    Calculate the support reactions of a simply supported beam.

    Args:
        span: Beam span in metres.
        loads: List of (magnitude, position) tuples.

    Returns:
        Tuple containing:
        - Reaction at A (kN)
        - Reaction at B (kN)
        - Total applied load (kN)
        - Applied load moment about A (kNm)
        - Equilibrium check (bool)

    Raises:
        ValueError: If the beam span is zero or negative.
    """

    if span <= 0:
        raise ValueError("Span can't be zero or negative")

    reaction_a = 0
    reaction_b = 0
    total_load = 0
    applied_moment_a = 0

    for magnitude, position in loads:
        # Influence line ordinates for support reactions
        ordinate1 = (span - position) / span
        ordinate2 = position / span

        # Superposition of individual load contributions
        reaction_a += ordinate1 * magnitude
        reaction_b += ordinate2 * magnitude
        total_load += magnitude
        applied_moment_a += magnitude * position

    # Equilibrium checks
    moment_check = applied_moment_a - (reaction_b * span)
    total_load_check = reaction_a + reaction_b - total_load

    equilibrium_check = (
        math.isclose(total_load_check, 0.0, abs_tol=1e-9)
        and math.isclose(moment_check, 0.0, abs_tol=1e-9)
    )

    return (
        reaction_a,
        reaction_b,
        total_load,
        applied_moment_a,
        equilibrium_check,
    )


# --------------------------------------------------
# AUTOMATED TEST RUNNER
# --------------------------------------------------

test_pass_counter = 0
test_case_no = 0
test_case_bools = []

for span, load_case, expected_r_a, expected_r_b, expected_error in test_cases:

    test_case_no += 1

    try:
        reaction_a, reaction_b, total_load, moment_a, equilibrium_check = (
            calculate_reactions(span, load_case)
        )

    except ValueError as e:
        print(f"Test Case {test_case_no}: {e}")

        # An expected exception means the test passed.
        overall_test_pass = expected_error

    else:
        if expected_error:
            # An exception was expected, but none occurred.
            overall_test_pass = False
            print(f"Test Case {test_case_no}: Expected ValueError was not raised.")

        else:
            # Normal reaction calculations
            reaction_a_test = math.isclose(
                reaction_a, expected_r_a, abs_tol=1e-9
            )

            reaction_b_test = math.isclose(
                reaction_b, expected_r_b, abs_tol=1e-9
            )

            overall_test_pass = (
                equilibrium_check
                and reaction_a_test
                and reaction_b_test
            )

            print(f"Span: {span:.2f}")
            print(f"Number of point loads: {len(load_case)}")

            if not load_case:
                print("Note: No point loads were supplied.")

            print(f"Total load: {total_load:.2f}")

            print(
                f"Calculated R_A: {reaction_a:.2f}; "
                f"Expected R_A: {expected_r_a}; "
                f"{'Ok!' if reaction_a_test else 'Not ok!'}"
            )

            print(
                f"Calculated R_B: {reaction_b:.2f}; "
                f"Expected R_B: {expected_r_b}; "
                f"{'Ok!' if reaction_b_test else 'Not ok!'}"
            )

            print(f"Applied moment about A: {moment_a:.2f}")
            print(f"Equilibrium Check: {'PASS' if equilibrium_check else 'FAIL'}")

    # Common reporting logic for both execution paths
    if overall_test_pass:
        test_pass_counter += 1

    test_case_bools.append((test_case_no, overall_test_pass))

    print("-------------------------------------------------------------------------")


# --------------------------------------------------
# TEST SUITE SUMMARY
# --------------------------------------------------

print("\nTEST SUITE SUMMARY")
print("------------------")

for case_no, test_result in test_case_bools:
    print(f"Test Case {case_no}: {'PASS' if test_result else 'FAIL'}")

print()
print(f"Tests passed: {test_pass_counter}/{len(test_cases)}")

all_tests_pass = (
    len(test_cases) > 0
    and test_pass_counter == len(test_cases)
)

print(f"Overall suite: {'PASS' if all_tests_pass else 'FAIL'}")
