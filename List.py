numbers=[25,12,36,95,14]
print(numbers)

numbers.append(70)
print("after append",numbers)

numbersc=numbers.copy()
print("after copy",numbersc)

y=numbers.count(95)
print("no. of 95",y)

numbers.extend([1,6])
print("after extend",numbers)

m=numbers.index(36,1,4)
print("index no of 36 is",m)

numbers.pop(3)
print("after pop",numbers)

numbers.remove(25)
print("after remove",numbers)

numbers.reverse()
print("after reverse",numbers)

numbers.sort()
print("after sort",numbers)
