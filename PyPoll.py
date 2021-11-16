# Add our dependencies.
import csv
# Assign a variable to load a file from a path.
file_to_load = 'election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = 'election_analysis.txt'

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)