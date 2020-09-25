# \n break line
myFile=open("fruits.txt")
#print(myFile.read())
#print(myFile.read())  #this will not read twice , tuis will create empty space

content=myFile.read()
myFile.close()
print(content)
print(content)

# x is used to create new file and write text
#with open("fruits.txt","x") as myFile:
    #myFile.write("okra")

with open("fruits.txt","a") as myFile:
    myFile.write("\nokra")
    #content=myFile.read() you cannot read ,coz you have given the parameter as a which is append
#print(content)

#to append and read at the same time
print("**************read file")
with open("fruits.txt","a+") as myFile:
    myFile.write("\nokra")
    myFile.seek(0) #since the cursor will be in last position , there is no content to read , so u r going to 0 position
    content=myFile.read()
print(content)