#_________________________________________________________________________________________________________________________________
# Topic: Data Type Casting in Rapid Diagnostic Test Features
# Description: Demonstrating how to convert string and float variables into proper formats (integer and float) for clinical data tracking.
# Application: Ensuring correct data types for kit inventory and analytical limits.
#_________________________________________________________________________________________________________________________________

device_id = '8812'
critical_concentration_of_antigen_to_get_positive = '1.25'
test_count_in_a_box = 25.0
test_count_in_a_box = int (test_count_in_a_box)
critical_concentration_of_antigen_to_get_positive = float (critical_concentration_of_antigen_to_get_positive)

print (test_count_in_a_box,critical_concentration_of_antigen_to_get_positive)
