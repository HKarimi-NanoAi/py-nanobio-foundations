# Topic: Cleaning DNA Sequence Data and Filtering Noise
# Description: Using 'for' and 'if' to filter out noise artifacts ('*' and '?') from a DNA sequence.
# Application: Pre-processing genetic sequences captured by optical or electrochemical biosensors before alignment or analysis.
#________________________________________________________________________________________________________________________________

cleaned_sequence = ""    #Attention = Do not put any spaces

uncleaned_dna_sequence = input("Enter the whole DNA sequence: ")

for component in uncleaned_dna_sequence:
    if component != "*" and component != "?":
        cleaned_sequence = cleaned_sequence + component

print(f"Your cleaned sequence is {cleaned_sequence}")
