print("average of three subjects with their total")

def average_total():
    subject1=float(input("enter marks of subject 1:"))
    subject2=float(input("enter marks of subject 2:"))
    subject3=float(input("enter marks of subject 3:"))
    total=subject1+subject2+subject3
    average=total/3
    print("total marks is:", total)
    print("average marks is:", average)

average_total()