s={"red","green","pink"}
print(s)

s.add("black")
print("after add",s)

p={"keys","green","chairs"}

m=s.difference(p)
print("after difference",m)

s.difference_update(p)
print("after difference_update",s)

s.discard("pink")
print("after discaring pink",s)

s.add("green")
k=s.intersection(p)
print("after intersection",k)

s.add("red")
s.add("black")
s.add("pink")
s.intersection_update(p)
print("after intersection_update",s)

p.remove("green")
w=s.isdisjoint(p)
print("after isdisjoint",w)

p.add("red")
r=s.issubset(p)
print("after issubset",r)

y=s.issuperset(p)
print("after issuperset",y)

s.add("yellow")
s.add("blue")
print("after pop",s)

q=s.symmetric_difference(p)
print("after symmetric_difference",q)

s.symmetric_difference_update(p)
print("after symmetric_difference_update",s)

t=s.union(p)
print("after union",t)

s.update(p)
print("after update",s)









