#creating an empty set

b = set()
print(type(b))

#adding values to an empty set
b.add(4)
b.add(5) #5 will rint only once in set, as it does not take multiple/duplicate values

b.add(5)#adding value repeatedly does not change a set

b.add(9)
'''
b.add([4, 5, 6,]) #give error as unhashable type: list
b.add({4,5,6}) #cannot add lists and dictionary to set

'''
print(b)
print(len(b))

b.remove(4) #removes 5 from the set b
# b.rmeove(15) # throws an error while trying to remove 15(which is not present in the set)
print(b)

print(b.pop())
print(b) #it will remove any element from set

b.clear()
print(b)
