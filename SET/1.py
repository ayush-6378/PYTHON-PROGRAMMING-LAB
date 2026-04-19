s1={'Math','Physics','Chemistry'}
s2={'Physics','Biology','Math'}
cm=s1.intersection(s2)
onlys1=s1.difference(s2)
onlys2=s2.difference(s1)
total=s1.union(s2)
print(f"common subjects :{cm}")
print(f"only student 1 : {onlys1}")
print(f"only student 2 : {onlys2}")
print(f"unique subjects : {total}")
