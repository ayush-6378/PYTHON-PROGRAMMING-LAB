data=[("john",),"alice",("mike",),"sarah",("david",)]
b=0
g=0
for i in data:
    if isinstance(i,tuple):
        b=b+1
    else:
        g=g+1
print(f"boys:{b},girls:{g}")
