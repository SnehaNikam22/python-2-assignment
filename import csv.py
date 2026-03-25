import csv

filename = "example.csv"

with open(filename, "r") as file:
    reader = csv.reader(file)
    
    rows = list(reader)   # Convert to list
    
    row_count = len(rows)
    column_count = len(rows[0]) if row_count > 0 else 0

print("Number of rows:", row_count)
print("Number of columns:", column_count)