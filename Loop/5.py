for a in range(1,31):
    for b in range(a,31):
        c=math.sqrt(a**2+b**2)
        if c<30 and c.is_integer():
            print(f"{a},{b},{int(c)})")
