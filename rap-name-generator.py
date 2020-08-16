# Guided Exploration No. 3
# Kris Smith

# Imports "random" library
import random

# List titled possible_names
possible_names = []

# Opens file named "rap-names-output.txt" to write in
outputFile = open('rap-names-output.txt', 'w')

# Opens file as a readable and assigns a handle to the file titled dataFile
with open('rap-names.txt', 'r') as dataFile:
    # Iterates through each line in file
    for name in dataFile:
        # Strips invisible line feed and appends name to possible_names list
        possible_names.append(name.rstrip())

# Asking user input for amount of rap names to be generated
count = int(input('How many rap names would you like to create? '))
# Asking user input for how many parts should names contain
parts = int(input('How many parts should the name contain? '))

for i in range(count):
    # List that will hold rap name parts
    name_parts = []
    # Iterate for number of rap names input by user
    for j in range(parts):
        # Generating random number to select random name and append to name_parts, -1 from random number to include 0
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

    # Write out generated rap names in file, glue each part using f string with a space, create new line with \n
    outputFile.write(f"{' '.join(name_parts)}\n")
    # Displays new name in terminal
    print(f"{' '.join(name_parts)}")

# Closes outputFile
outputFile.close()
