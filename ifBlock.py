def mean(value):
  if type(value)==dict:
     the_mean=sum(value.values())/len(value)
     return the_mean
  else:
      the_mean=sum(value)/len(value)
      return the_mean

student_grades={"Ananth": 9.1 , "Priya" :8.8 , "Kirithik" :7.5}
print(mean(student_grades))

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")

x = 1
y = 1
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")

a=3>1
print(a)
if(a==True):
    print ("greater")
else:
    print ("smaller")

b=None
if(b==None):
    print("None")

x=None
if isinstance(x, int) or isinstance(x, float) or x=='1':
    print("Valid type!")
else:
    print("Not valid!")


if(1>3):
    print("smaller")
else:
    print("greater")


x=3
y=7
if x>y:
    print("x is greater than y")
elif x==y:
    print ("x is equal to y")
else:
    print("x is less than y")