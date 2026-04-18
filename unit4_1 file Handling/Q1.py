import csv
import os

filename = "students.csv"

# Constraint: Create file and write specific text if it doesn't exist
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG the quick brown fox jumps over the lazy dog\n")

# Main Program: Append CSV data
# Opening in 'a' (append) mode so we don't overwrite the requested string
with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    # Writing headers and some sample data
    writer.writerow(['rollno', 'name', 'marks_sub1', 'marks_sub2', 'marks_sub3'])
    writer.writerow([101, 'Alice', 85, 90, 88])
    writer.writerow([102, 'Bob', 78, 82, 80])
    
print(f"Data successfully written to {filename}. You can open this in MS-Excel.")