import os
import shutil

source_dir = "source_folder"
target_dir = "target_folder"
source_file = os.path.join(source_dir, "my_file.txt")

# Create directories
os.makedirs(source_dir, exist_ok=True)
os.makedirs(target_dir, exist_ok=True)

# Constraint: Create source file with specific text if it doesn't exist
if not os.path.exists(source_file):
    with open(source_file, 'w') as f:
        f.write("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG the quick brown fox jumps over the lazy dog\n")

# Main Program: Copy the file
target_file = os.path.join(target_dir, "my_file.txt")
shutil.copy(source_file, target_file)

print(f"File copied from {source_dir} to newly created subdirectory {target_dir}.")