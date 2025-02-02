#Sets & its operations
#listing out the legends
legends = {'kannadasan','valli','msv'}

legends.add('mr radha')
print(legends)

add =['nagash','sivaji','boss','msv','valli']
legends1 =set(add)
print(legends1)

legends1.remove('boss')
print(legends1)

#names in both groups
print(legends.union(legends1))

#same name in both groups
print(legends.intersection(legends1))

#name only in one group
print(legends.difference(legends1))

legends1.clear()
print(legends1)