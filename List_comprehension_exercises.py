def printNumbers(myList):
    new_temps=[temp for temp in myList if type(temp)!=str]
    return new_temps #this will return only integers and not string


print(printNumbers([1,2,'A']))

#Another Method
def foo(lst):
    return [i for i in lst if not isinstance(i, str)]

print(foo([3,2,5,'a']))



def myList(list):
    new_list=[i if not isinstance(i, str) else 0 for i in list]
    return new_list
print(myList([1,2,'A']))



def sumStrings(myList):
   return sum([float(i) for i in myList])

print(sumStrings(['1.2','1.5','1.3']))


     
  