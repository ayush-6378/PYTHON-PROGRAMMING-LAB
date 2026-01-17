print("inteerest calculator")

def interest_calculator():
    principal=float(input("enter principal amount:"))
    rate=float(input("enter rate of interest:"))
    time=float(input("enter time in years:"))
    interest=(principal*rate*time)/100
    print("interest is:", interest)

interest_calculator()