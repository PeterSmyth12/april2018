# Lists

#create an empty list
myList = []

#create list with values
myList2 = [ 5,8,9]

# Items in the list don't all have to be the same type
myList3 = ['Hello', 42, 3.142 ]

# individual elements in the list can be referenced

print ("\nExample 1\n")
print ("\nmyList3[0]\n")
print (myList3[0])

# to iterate over all of the elements in a list
print ("\nExample 2\n")
print ("\nto iterate over all of the elements in a list\n")
for x in myList3 :
    print (x)

#to add an element
print ("\nExample 3\n")
myList3.append("new item")
print ("\n myList3 after adding an item to the end\n")
for x in myList3 :
    print (x)

# how many items in the list
print ("\nExample 4\n")
print ("\nHow many elements in a list\n")
print (len(myList3))

# print last element remembering that the indexing starts at 0
print ("\nExample 5\n")
print ("\nprint last element remembering that the indexing starts at 0\n")
print (myList3[len(myList3) - 1])

# or more simply (counting backwards from the end)
print ("\nExample 6\n")
print ("\n or more simply (counting backwards from the end)\n")
print (myList3[-1])

#to delete an item
print ("\nExample 7\n")
print ("\n myList3 before deleting item at index 2\n")
for x in myList3 :
    print (x)
del myList3[2]
print ("\n myList3 after deleting an item\n")
for x in myList3 :
    print (x)


