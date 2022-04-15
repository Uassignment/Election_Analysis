# The data we need to retrive
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The  percentage of votes each candidate won
# 4. The total number of votes each candidate received
# 5. The winner of the election based on popular vote
# Import the datetime class from the datetime module.


# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

import csv

import os


# Assign a variable for the file to load and the path.
#file_to_load = 'Resources\\election_results.csv'

file_to_load = os.path.join("Resources","election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")


#Open the election results and read the file. 
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

#Close the file.

#election_data.close()

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:


# Write some data to the file.
#outfile.write("Hello World")
    #txt_file.write("Hello World")

# Write three counties to the file.
    # txt_file.write("Arapahoe ")
    # txt_file.write("Denver ")
    # txt_file.write("Jefferson")
    #add comma in between countries
    #txt_file.write("Arapahoe, Denver, Jefferson")
    #print in new line
    # txt_file.write("Counties in the Election\n")
    # txt_file.write("--------------------------\n")
    # txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
# Read and print the header row.
    headers = next(file_reader)
    print(headers)