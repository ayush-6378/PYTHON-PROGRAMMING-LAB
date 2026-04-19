import math
n=int(input("enter a number"))
is_prime=n>1 and all(n%i !=0 for i in range(2,int(math.sqrt(n))+1))
is_perfect=sum(i for i in range(1,n) if n%i==0)==n
s=str(n)
is_armstrong=sum(int(d)**len(s) for d in s)==n
is_palindrome=s==s[::-1]
is_automorph=str(n*n).endswith(s)
print(f"prime:{is_prime},perfect:{is_perfect},armstrong:{is_armstrong},palindrome:{is_palindrome},automorphic:{is_automorph}")
        


