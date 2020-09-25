with open("fruits.txt","r") as myFile:
    content=myFile.read()    
    myFile.close() #not mandatory , with keyword will take care of closing the file automatically
print(content)

with open("fruits.txt") as myFile:
    content=myFile.read()    
print(content)


with open("vegetables.txt","w") as myFile:
    myFile.write("tomato\ncucumber\nOnion")  
    myFile.write("Garlic")  #immediately after onion , there is no spaec , you will see garlic
print(content)

#Read first 90 characters in a file
with open("bear.txt","r") as myFile:
    content=myFile.read()    
print(content[:90])

#count no of characters in a file
def countOccurances(ch,filePath="bear.txt"):
    myFile=open(filePath)
    content=myFile.read()
    return content.count(ch)

#create a file file.txt and write text snail
with open("file.txt","w") as myFile:
    myFile.write("snail") 

#read first 90 characters from bear.txt and paste in first.txt
with open("bear.txt","r") as myFile1:
    content=myFile1.read()
with open("first.txt","w") as myFile2:
    myFile2.write(content[:90])

#copy the content of bear1 text and append to bear 2
with open("bear1.txt","r") as myFile1:
    content=myFile1.read()
with open("bear2.txt","a") as myFile2:
    myFile2.write(content)

# read the content of read1.txt and append at end to same file again 2 times
with open("read1.txt","a+") as myFile1:
    content=myFile1.read()
    myFile1.write(content)
    myFile1.write(content)



    


