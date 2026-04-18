import csv
import os

filename = "student_data.csv"

# Constraint: Create file with specific text and some valid CSV data to read
if not os.path.exists(filename):
    with open(filename, 'w', newline='') as f:
        f.write("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG the quick brown fox jumps over the lazy dog\n")
        # Adding sample data so the reading logic works
        writer = csv.writer(f)
        writer.writerow(['rollno', 'name', 'm1', 'm2', 'm3'])
        writer.writerow(['1', 'John Doe', '75', '80', '95'])

student_dict = {}

# Main Program: Read and process
with open(filename, 'r') as f:
    reader = csv.reader(f)
    lines = list(reader)
    
    # Skip the dummy text line if it's there
    start_index = 1 if "QUICK BROWN FOX" in lines[0][0] else 0
    
    # Process rows after headers
    for row in lines[start_index + 1:]:
        if len(row) >= 5:
            rollno = row[0]
            name = row[1]
            marks = [int(row[2]), int(row[3]), int(row[4])]
            total = sum(marks)
            
            student_dict[rollno] = {
                'name': name,
                'marks': marks,
                'total': total
            }

print("Student Dictionary Data:")
for roll, data in student_dict.items():
    print(f"Roll No: {roll} -> {data}")