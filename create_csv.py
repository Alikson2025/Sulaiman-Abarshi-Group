import csv

csv_file = [
    ["Email", "Area_of_Interest"],
    ["sulaimanabarshi5@gmail.com", "Genomics"],
    ["abdulkadiryau229@gmail.com", "Machine Learning in Bioinformatics"],
    ["adamuusmanmaimsa@gmail.com", "Structural Bioinformatics"],
    ["alhajihassanhashimu@gmail.com", "Bioinformatics tool development"],
    ["balkisuibrahimsanda@gmail.com", "System biology"],
    ["muhammadsalehhassana@gmail.com", "Metagenomics"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_file)
print("CSV file 'data.csv' created successfully")