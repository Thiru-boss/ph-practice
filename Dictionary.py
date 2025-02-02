#Dictionary
'''listing top old bikes'''
bikes = {1:['re',350],2:'jawa','3':['yamaha rx',100]}

print('total brands:',len(bikes))
#bike names
print(bikes.values())
#list the brand number with names
print(bikes.items())
#adding another brand
bikes[4] = 'suzuki',100
print(bikes)

#secondry brand list
bikes = dict({1:'diesel bullet'})
print(bikes)