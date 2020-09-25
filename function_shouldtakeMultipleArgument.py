def mean(*args):
   # return type(args)
   return sum(args)/len(args)


print(mean(1,2,3))



def print_Strings(*args):
    sorted_list=[i.upper() for i in args]
    return sorted(sorted_list)


print(print_Strings('snow','glacier','iceberg'))

#keyword arguments

def mean(**kwargs):
    return kwargs
print(mean(a=1,b=2,c=3))
#you get dictionary {'a': 1, 'b': 2, 'c': 3}

#this will returm sum 9
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=6,b=3))