import csv
# Assign a variable for the file to load and the path.
file_to_load = 'election_results.csv'
election_data = open(file_to_load, 'r')
election_data.close()
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

     import textwrap
# Assign a variable for the file to load and the path.
file_to_save = 'election_Analysis.txt'
election_analysis = open(file_to_save,'w')
election_analysis.close()
# Open the election results and read the file.
with open(file_to_save) as election_analysis:

    # Print the file object.
     print(election_analysis)


     outfile = open(file_to_save, "w")
     outfile.write("Hello World")
     outfile.close()
     print(outfile)