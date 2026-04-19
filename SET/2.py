d1={101,102,103,104}
d2={103,104,105,106}
both=d1.intersection(d2)
onlyod=d1.symmetric_difference(d2)
uniq=d1.union(d2)
print(f"visited both days :{both}")
print(f"visited only one days :{onlyod}")
print(f"total unique visitors  :{uniq}")
