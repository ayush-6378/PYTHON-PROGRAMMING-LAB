import os

file1 = "file1.txt"
file2 = "file2.txt"
merged_file = "merged.txt"

# Constraint: Ensure both files exist with the text
for f_name in [file1, file2]:
    if not os.path.exists(f_name):
        with open(f_name, 'w') as f:
            f.write("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG the quick brown fox jumps over the lazy dog\n")
            f.write(f"Extra line 1 in {f_name}\n")
            f.write(f"Extra line 2 in {f_name}\n")

# Main Program: Merge alternatively
with open(file1, 'r') as f1, open(file2, 'r') as f2, open(merged_file, 'w') as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    
    max_length = max(len(lines1), len(lines2))
    
    for i in range(max_length):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])

print(f"Files merged successfully into {merged_file}.")