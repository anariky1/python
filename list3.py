monday_temperatures=[9.1,8.8,5.5,6.5,7.5]
monday_temperatures.append(4.2)
print(monday_temperatures)
"clears the list"
#monday_temperatures.clear()
print(monday_temperatures)

#index-----------------
print(monday_temperatures.index(5.5))
print(monday_temperatures.index(8.8,1)) # you are startind to find 8.8 from index position 1

#print(monday_temperatures.index(8.8,2)) # you are startind to find 8.8 from index position 2

#get item from index
print(monday_temperatures.__getitem__(2))
print(monday_temperatures[2]) #same as above
print(monday_temperatures[1:3]) # it will retrieve 2nd index to 3-1 index
print(monday_temperatures[0:3])
#this is same as below - shortcut
print(monday_temperatures[:3])
print(monday_temperatures[2:])

print("negative indexing")

print(monday_temperatures[-1])
print(monday_temperatures[-5:-2]) #last index is -5 