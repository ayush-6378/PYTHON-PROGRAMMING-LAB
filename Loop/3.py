text=input("enter a string")
alpha=sum(c.isalpha() for c in text )
digits=sum(c.isdigit() for c in text)
print(f"alphabets:{alpha},digits:{digits}")
