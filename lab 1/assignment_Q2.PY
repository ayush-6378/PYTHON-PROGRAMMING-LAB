print("swapping 2 numbers using 3rd variable")

def swap_numbers():
    a=float(input("enter first number:"))
    b=float(input("enter second number:"))
    print("before swapping a is:", a)
    print("before swapping b is:", b)
    temp=a
    a=b
    b=temp
    print("after swapping a is:", a)
    print("after swapping b is:", b)

swap_numbers()