# sum average grade allotment 
def grade_calc():
    print("enter marks of 3 subject\n")
    sub1=int(input("enter marks of sub 1 out of 100:"))
    sub2=int(input("enter marks of sub 2 out of 100:"))
    sub3=int(input("enter marks of sub 3 out of 100:"))
    sum=sub1+sub2+sub3
    print("total of all 3 subjects:",sum)
    avg=sum/3
    print("average of marks:",avg)
    if sub1>=35 and sub2>=35 and sub3>=35:
        print("Student passed all subjet")
    else:
        print("student fail")
    

    def grade_allot(sub):
        
        if 0<=sub<=39:
            print("Grade=F")
        elif 40<=sub<=44:
            print("Grade=P")
        elif 45<=sub<=49:
            print("Grade=c")
        elif 50<=sub<=54:
            print("Grade=B")
        elif 55<=sub<=59:
            print("Grade=B+")
        elif 60<=sub<=69:
            print("Grade=A")
        elif 70<=sub<=79:
            print("Grade=A+")
        elif 80<=sub<=100:
            print("Grade=O")
        else:
            print("Grade=NA(absent)")
    print("...................result...................")    
    print("subject1 marks, grade",sub1,grade_allot(sub1))
    print("subject2 marks, grade",sub2,grade_allot(sub2))
    print("subject3 marks, grade",sub3,grade_allot(sub3))
        


grade_calc()


    

