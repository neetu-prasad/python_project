myDict = {
"Fast": "in a quick manner",
"monkey": "an animal",
"anotherdict" : {'harry': 'player'}
}
#dictionary methods
print(list(myDict.keys()))  #prints the keys of the dictionary
print(myDict.values()) #prints the values of the dictionary
print(myDict.items())   #prints the keys, values for all contents of the dictionary
print(myDict)

updateDict = {

    "Lovish": "Friend" ,
    "veeru" : "kuchb" ,
    "neetu" : "kuchnahi" ,
    "monkey": "a bird" #it will update the value of monkey in first list of dictionery

}
myDict.update(updateDict)
print(myDict)

print(myDict.get("monkey"))#prits value associated with key
print(myDict["monkey"]) #prits value associated with key

#difference btwn .get and [] syntax
print(myDict.get("monkey2"))#Returns none as monkey2 is not present in dictionary
print(myDict["monkey2"]) # throws an error as monkey2 is not present in dictionary

#why to use .get method as we can ge it simpl 
#we can get same output by the above methods to get values if list name is correct
# but, if list name is not correct .get function will return none as o/p whereas secnd one will get error
#so its better to use get method

