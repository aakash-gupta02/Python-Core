l = [12,34,121,-34,-4,23,-32,1,2111,-2,500]

# avg = 0

# print("Positive elements are: ")
# for i in l:
#     if i >0:
#         print(i)


# print("Negative elements are: ")
# for i in l:
#     if i < 0:
#         print(i)



# for i in l:
#     avg += i


# # print(len(l))
# print(f"Average is:{avg/len(l)} ")

# largest = l[0]
# index = 0

# for i in range (len(l)):
#     if largest < l[i]:
#         largest = l[i]
#         index = i

# print(f"largest is: {largest} at index {index} ")


large = l[0]
secLarge = l[0]

for i in l:
    if large < i:
        secLarge = large
        large = i


print(f"largest is {large}, Second Largest is {secLarge}")  
