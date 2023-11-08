list = ['Pilot' , 'Deli' , 'Muji' , 'Mechanical' ,]
list.append('Sharpie')
pop = list.pop(3)
del list[0]
print(pop)
print(list)


Beers = ['Budweiser' , 'Guiness' , 'San Miguel' , 'Sapporo']
Beers.append('Heineken')
list = Beers.pop(0)
list2 = Beers.pop(3)
print(list)
print(list2)

# still dk how to use define func but anyways
def add_one(input):
    output = input + 1
    return output
