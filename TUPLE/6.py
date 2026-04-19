tup=(10,20,30)
lst=list(tup)
lst[1]=25
newtup=tuple(lst)
print("original:",tup)
print("modified:",newtup)
