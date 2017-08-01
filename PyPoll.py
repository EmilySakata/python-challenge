import os
import csv

count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0


# Establish the root path and resource path
root_path = os.getcwd()
resource_path = os.path.join(root_path, "raw_data")

# Iterate through the listdir results
filepaths = []
for file in os.listdir(resource_path):
    if file.endswith(".csv"):
        filepaths.append(os.path.join(resource_path, file))

# Read each csv into a dictionary and 

for file in filepaths:
    new_poll_data = []

#Merge data from multiple fileset

# Read each csv file and append the contents to the new_poll_data list
for file in filepaths:
    with open(file, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csvdata = list(csvreader)
        # @NOTE: We use index slicing to skip the header line from each file
        new_poll_data.extend(csvdata[1:])

# * The total number of votes cast
for i in new_poll_data:
	count = count +1
total_number = round(count)
# print(total_number)
# * A complete list of candidates who received votes

list = []
for j in new_poll_data:
	candidate = j[2]
	if candidate not in list:
		list.append(candidate)

# count the numberof votes for the candidate
for k in new_poll_data:
	candidate = k[2]
	if candidate == list[0]:
		count1 = count1+1
	elif candidate == list [1]:
		count2 = count2+1
	elif candidate == list [2]:
		count3 = count3 +1
	elif  candidate == list[3]:
		count4 = count4 +1

#Create dictionary
vote = {list[0]:count1, list[1]: count2, list[2]: count3, list[3]:count4}

# print(vote)


# * The percentage of votes each candidate won
percent_vote = {list[0]: round(count1/total_number*100,0),list[1]: round(count2/total_number*100,0), list[2]: round(count3/total_number*100,0), list[3]:round(count4/total_number*100,0)}
# print(percent_vote)
# * The total number of votes each candidate won

# * The winner of the election based on popular vote.
max_value = max(vote.values())  # maximum value
max_keys = [k for k, v in vote.items() if v == max_value] # getting all keys containing the `maximum`

# print(max_keys, max_value)

# ```
# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------
# ```

print("Election Result")
print(f"total Votes:{total_number}")
print(f"Number of votes for each candidate: {vote}")
print (f"Percent of votes for each candidate: {percent_vote}")
print(f"Winner: {max_keys}")

# Write the calculated data to a new file.
output_path = os.path.join(root_path, "output")
csvpath = os.path.join(output_path, "PollSummary.csv")
with open (csvpath, "w", newline="") as csvfile:
	fieldnames = ["Candidate", "percent", "vote"]   
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# writer.writeheader()
writer.writerow({"Candidate": list[0], "percent": round(count1/total_number*100,0), "vote": count1})
writer.writerow({"Candidate": list[1], "percent": round(count2/total_number*100,0), "vote": count2})
writer.writerow({"Candidate": list[2], "percent": round(count3/total_number*100,0), "vote": count3})
writer.writerow({"Candidate": list[3], "percent": round(count4/total_number*100,0), "vote": count4})


