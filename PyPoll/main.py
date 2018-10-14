#import the necessary modules
import os
import csv
file_to_output = os.path.join("PyPoll.txt")
NameofCandidates = []
total = 0
#read in csv file
election_csv = os.path.join("election_data.csv") 
with open(election_csv, 'r') as electioncsv:
    electionreader = csv.reader(electioncsv, delimiter = ",")
    csv_header = next(electionreader)
    TotalVotes = 0
    KhanVotes = 0
    CorreyVotes = 0
    LiVotes = 0
    OTooleyVotes = 0
    for row in electionreader:   
        TotalVotes = TotalVotes + 1
        if row[2] not in NameofCandidates:
            NameofCandidates.append(row[2])
        if row[2] == "Khan":
            KhanVotes = KhanVotes + 1
        if row[2] == "Correy":
            CorreyVotes = CorreyVotes + 1
        if row[2] == "Li":
            LiVotes = LiVotes + 1
        if row[2] == "O'Tooley":
            OTooleyVotes = OTooleyVotes + 1
    KhanPercentage = round((KhanVotes/TotalVotes)*100)
    CorreyPercentage = round((CorreyVotes/TotalVotes)*100)
    LiPercentage = round((LiVotes/TotalVotes)*100)
    OTooleyPercentage = round((OTooleyVotes/TotalVotes)*100)


    print(TotalVotes)
    print(NameofCandidates)
    print(KhanVotes)
    print(CorreyVotes)
    print(LiVotes)
    print(OTooleyVotes)
    print(KhanPercentage)
    print(CorreyPercentage) 
    print(LiPercentage) 
    print(OTooleyPercentage) 

output = (
    f"\nPyPoll Analysis\n"
    f"-------------------------\n"
    f"Total Votes: {TotalVotes}\n"
    f"Name of Candidates: {NameofCandidates}\n"
    f"Votes for Khan: {KhanVotes}\n"
    f"Votes for Correy: {CorreyVotes}\n" 
    f"Votes for Li: {LiVotes}\n" 
    f"Votes for OTooley: {OTooleyVotes}\n"
    f"Votes for Khan (%): {(KhanPercentage)}\n"
    f"Votes for Correy(%): {(CorreyPercentage)}\n"
    f"Votes for Li(%): {(LiPercentage)}\n"
    f"Votes for OTooley(%): {(OTooleyPercentage)}\n")
 
 
print(output)    

#Save the results to analysis text file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output)

