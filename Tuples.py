#Tuples
'''buying fruits'''
from operator import index

fruits = ("mango","banana","apple")
print(fruits)
print('total fruits:', len(fruits))

'''buying one more fruit'''
fruits = fruits + ('kiwi',)

#using Traversal to list the fruits
for i in fruits:
    print(i)
print()

'''fruits mentions as kg'''
fruits = (2,7,10,4)

'''finding in min and max of fruits kgs'''
print('min kg:', min(fruits))
print('max kg:', max(fruits))

'''finding the order of the apple'''
print('order of apple:', fruits.index(10))

'''Count of how many times kiwi was bought'''
print('Count kiwi:', fruits.count(4))

