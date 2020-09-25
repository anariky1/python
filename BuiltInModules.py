username='pypypy'
print(len(username))
print(username.count('p'))

#this will read infinity times and print the content infinity times
#while True:
   # with open("vegetables.txt") as file:
      #  print(file.read())
        # control+c to terminate

#there is no built in function to terminate
import time
import os

while True:
   if os.path.exists("vegetables.txt"):
        with open("vegetables.txt") as file:
          print(file.read())
   else:
        print("file doesnt exist")
   time.sleep(10)