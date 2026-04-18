# Dictionary format: { roll_no : [dept_no, salary] }
employees = {
    101: ['HR', 50000],
    102: ['IT', 60000],
    103: ['HR', 45000],
    104: ['IT', 75000],
    105: ['Finance', 55000]
}

# Create a new dictionary to group salaries by department
# Format will be: { 'HR': [50000, 45000], 'IT': [60000, 75000]... }
dept_salaries = {}

for roll_no in employees:
    dept = employees[roll_no][0]
    salary = employees[roll_no][1]
    
    # If we haven't seen this department yet, add it with an empty list
    if dept not in dept_salaries:
        dept_salaries[dept] = []
        
    # Add the salary to that department's list
    dept_salaries[dept].append(salary)

# Now loop through our grouped dictionary to find min and max
print("Department-wise Salary Report:")
for dept in dept_salaries:
    salaries_list = dept_salaries[dept]
    
    min_sal = min(salaries_list)
    max_sal = max(salaries_list)
    
    print("Dept:", dept, "| Min Salary:", min_sal, "| Max Salary:", max_sal)