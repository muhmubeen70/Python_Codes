import csv

with open("data.csv", 'w') as csv_file:
    Rows = ["col1", "col2"]
    writer = csv.DictWriter(csv_file, fieldnames=Rows)
    writer.writeheader()
    writer.writerow({"col1": "Muhammad",  "col2": "Mubeen"})
    writer.writerow({"col1": "Ahmad",     "col2": "Maqsood"})
    writer.writerow({"col1": "mustafa",   "col2": "Hamad"})
    writer.writerow({"col1": "Muhammad",  "col2": "Nawaz"})
    writer.writerow({"col1": "Sheharyar", "col2": "Khan"})
    writer.writerow({"col1": "Muhammad",  "col2": "Yaseen"})
    writer.writerow({"col1": "Noor",      "col2": "Muhammad"})
    writer.writerow({"col1": "Chaudhry",  "col2": "Umair"})
    writer.writerow({"col1": "Ahmad",     "col2": "Hassan"})
    writer.writerow({"col1": "Anwaar",    "col2": "Ulhassan"})
