myDict = {

    "Pankha" : "fan" ,
    "Dabba" : "Box" ,
    "Vastu" : "Item"
}


print("options are : ", myDict.keys())
a = input("Enter the Hindi word \n")
#print("The meaning of your word is :" , myDict[a])

#below line will not throw an error if the key is not present in the dictionary
print("the meaning of the word is:", myDict.get(a))
