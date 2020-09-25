temps=[221,220,340,230]

new_temps=[]
for temp in temps:
    new_temps.append(temp/10)

print(new_temps)

#Another way
new_temps1=[temp/10 for temp in temps]
print(new_temps1)

print("remove -9999")
temps2=[221,220,-9999,230]
new_temps2=[temp/10 for temp in temps2 if temp!=-9999]
print(new_temps2)

#I want to print 0 instead of -9999 - the below syntax is wrong
#temps3=[221,220,-9999,230]
#new_temps3=[temp/10 for temp in temps if temp!=-9999 else 0]
#print(new_temps3)

#I want to print 0 instead of -9999 - the below is correct syntax
temps4=[221,220,-9999,230]
new_temps4=[temp/10  if temp!=-9999 else 0 for temp in temps4]
#if temp is <> -9999 , put in new_temp4 , else replace -9999 with 0
print(new_temps4)
# for loop is at very end 
