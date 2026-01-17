print("net sales calculator")

def net_sales():
    gross_sales=float(input("enter gross sales:"))
    discounts=gross_sales*0.1
    net_sales=gross_sales-discounts
    print("net sales is:", net_sales)

net_sales()