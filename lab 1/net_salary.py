print("enter net salary calculator")

def net_salary():
    gross_salary=float(input("enter gross salary:"))
    deductions=gross_salary*0.03
    allowance=gross_salary*0.1
    net_salary=gross_salary+allowance-deductions
    print("net salary is:", net_salary)

net_salary()