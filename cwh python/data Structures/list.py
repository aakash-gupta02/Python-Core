myList = [12,34,12,565,32,"aakash"]
mixed = [12,"sky", 12.12, "gfx",212]


print(myList)
print(mixed)

print(myList[1])

print(mixed[1::-1])


# list methods....
print("List methods")

myList.append("sdsd")
myList.pop()

myList.insert(2,"aakash")

print(myList.count("aakash"))

myList.reverse()
# myList.sort()

myList.extend(mixed)

print(myList)
