def area(a,b):
    print(b)
    print(a)
    return a*b

#print(area(3,4))
# non keyword arguments

print(area(b=3,a=4)) #keyword argumments

# method 2
def area_parameter(a,b=6):
#def area_parameter(b=6 ,a): #syntax is wrong - Non default argument follows default argument - non assigned should be
                             #first argument
    return a*b

print(area_parameter(3))  # you are passing only one argument thpugh there are 2 parameters
print(area_parameter(3,b=7))   # b will be 7


