def avg1(a,b,c):
    d = a +b+c/3
    print(d)  #using print


def avg2(a,b,c):
    d = a +b+c/3
    return d     #using return


def avg3(a=0,b=0,c=0): #b=0 is a default values 
    d = a+b+c/3
    return d




a1 = avg1(12,324,656)    
a2 = avg2(123,324,656)    

print(avg3())


a3 = avg2(b=28, c=25,a=23)   # specifically telling which values is for which paramters
print(a3)

# print(a1)
print(a2)





# lambda function...


squ = lambda x: x*x # single parameter

sum = lambda x, y: x+y # multiple parameters



print(squ(7))
print(sum(2323,2324))

