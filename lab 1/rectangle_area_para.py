print("rctangle area and perimeter calculator")

def rectangle_area_para():
    length=float(input("enter length of rectagle:"))
    breadth=float(input("enter breadth of rectangle:"))
    area=length*breadth
    perimeter=2*(length+breadth)
    print("area of rectangle is:", area)
    print("perimeter of rectangle is:", perimeter)
    
rectangle_area_para()