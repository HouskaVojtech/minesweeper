coordinates = (2,2)

print(type(coordinates))

helper_numbers = [-1,0,1]
for i in helper_numbers:
    for j in helper_numbers:
        if i or j: 
            print ( coordinates[0] + i, coordinates[1] + j )
