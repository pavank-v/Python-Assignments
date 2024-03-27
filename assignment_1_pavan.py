# LISTS

mylist = [10, 20, 30, 40, 22, 50, 60, 15, 70, 80, 90]

# Printing available methods for lists
print(dir(mylist))

# Appending 100 to the list
mylist.append(100)
print(mylist)

# Clearing the list
mylist.clear()
print(mylist)

# Copying the cleared list to a new list
newlist = mylist.copy()
print(newlist)

# Counting occurrences of 10 in the list
print(mylist.count(10))

# Extending the list with another list
mylist2 = [110, 120]
mylist.extend(mylist2)
print(mylist)

# Finding the index of 20 in the list
print(mylist.index(20))

# Inserting 15 at index 1
mylist.insert(1, 15)
print(mylist)

# Removing the last element from the list
mylist.pop(-1)
print(mylist)

# Removing 110 from the list
mylist.remove(110)
print(mylist)

# Reversing the list
mylist.reverse()
print(mylist)

# Sorting the list
mylist.sort()
print(mylist)



# TUPLE

mytuple = (10, 15, 20, 30, 40, 22, 50, 60, 15, 70, 80, 90)

# Printing available methods for tuples
print(dir(mytuple))

# Counting occurrences of 15 in the tuple
print(mytuple.count(15))

# Finding the index of 80 in the tuple
print(mytuple.index(80))

# Sorting the tuple (Note: tuples are immutable, so sorted() creates a new sorted list)
sorted(mytuple)



# DICTIONARY

mydict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# Printing available methods for dictionaries
print(dir(mydict))

# Getting dictionary values
print(mydict.values())

# Updating the dictionary with a new key-value pair
mydict.update({6: 'six'})
print(mydict)

# Setting a default value for an existing key
mydict.setdefault(1, 'new')
mydict.setdefault(0, 'zero')
print(mydict)

# Removing and returning an arbitrary key-value pair
mydict.popitem()
print(mydict)

# Removing the key 5 from the dictionary
mydict.pop(5)
print(mydict)

# Getting dictionary keys
print(mydict.keys())

# Getting dictionary items
print(mydict.items())

# Iterating through dictionary items
for i, j in mydict.items():
    print(i, j)

# Getting the value for key 4
print(mydict.get(4))

# Creating a new dictionary from keys with a default value
keys = [1, 2, 3, 4]
valuedefault = 0
mydict2 = dict.fromkeys(keys, valuedefault)
print(mydict2)

# Copying the dictionary
newdict = mydict.copy()
print(newdict)

# Clearing the dictionary
mydict.clear()
print(mydict)
