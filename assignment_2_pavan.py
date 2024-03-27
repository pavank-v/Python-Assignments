'''NESTED DICTIONARY'''

#Nested Dictionary
college={'student':{'student_name':'sam'},'professor':{'professor_name':'john'}}

#Reading Value
college['student']['student_name']

#Assigning new value to key
college['student']['student_id']=123

#printing the current dictionary
print(college)

#Another Nested Dictionary
college2={'course':{'name':'java'}}

#Combining Two nested Dictionary
college.update(college2)

#Printing the Dictionary
print(college)

#Deleting a Key
del college['course']['name']

#Printing the Dictionary
print(college)

del college['course']
print(college)

'''SETS'''
#Empty set
myset = set()

print(dir(myset))

#Creating a Set
myset={'java','python','r','c','ruby'}

#Another Set
myset2={'java','ruby','kotlin','c++'}

#Adding Element in Set
myset.add('c#')
print(myset)

#Difference
print(myset.difference(myset2))

#Intersection
print(myset.intersection(myset2))

#Disjoint
print(myset.isdisjoint(myset2))

#Subset
print(myset.issubset(myset2))

#Superset
print(myset.issuperset(myset2))

#Symmetric Difference
print(myset.symmetric_difference(myset2))

#Union
print(myset.union(myset2))

#Updating the Set
myset.update(myset2)
print(myset)


'''If, elif and else condition.'''

'''Python program to check the grade based on marks'''
marks=90
if marks > 90:
    print('A')
elif marks > 80 and marks <= 90:
    print('B')
elif marks > 70 and marks <= 80:
    print('C')
else:
    print('D')
    
    
'''For loop with range, enumerate, continue and break'''

for i , j in enumerate(range(10)):
    if j == 5:
        continue
    elif j == 9:
        break
    print(i , 2*j)