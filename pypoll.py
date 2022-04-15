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

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]


        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        #Add the candidate name to the candidate list.
        #candidate_options.append(candidate_name)

# 3. Print the total votes.

#print(total_votes)      

# Read and print the header row.
    # headers = next(file_reader)
    # print(headers)
# Print the candidate list.
#print(candidate_options)
# Print the candidate vote dictionary.
#print(candidate_votes)
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage}% of the vote.")

# Determine winning vote count and candidate
# Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)