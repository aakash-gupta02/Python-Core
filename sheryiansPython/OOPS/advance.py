# # comprehension()


# square = [i*i for i in range(10) ]
# print(square)


# even2 = {i for i in range(20) if i%2 ==0 }

# print(even2)


# # lambda


# squ = lambda x: x*x

# print(squ(59))

# compre ques


numList = [i for i in range(11)]
print(numList)

even20 = [i for i in range(21) if i % 2== 0  ]
print(even20)

nums = [-5, 3, -1, 8, -2, 0, 6]

posi = [i  for i in nums if i >0 ]
print(posi)

words = ["apple", "banana", "cherry"]

upperCased = [i.upper() for i in words  ]
print(upperCased)


sentence = "Python is super fun"

lengthSen = [len(i) for i in sentence.split(" ") ]

print(lengthSen)


add = lambda x: x + 10

print(add(20))

lamEven = lambda x: x % 2== 0
print(lamEven(4))


numsww = [1, 2, 3, 4]

doubled = map(lambda x: x*2, numsww)
print(list(doubled))


odd = filter(lambda x: x%2 != 0, numsww  )

print(list(odd))


# pairs = [(1, 3), (2, 1), (4, 2)]

# sortBy2 = sorted(lambda )