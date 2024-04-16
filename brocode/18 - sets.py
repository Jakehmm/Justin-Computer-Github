# set = collection which is unordered, unindexed. No duplicate values

utensils = {"Spoon" , "Fork" , "Knife"}
dishes = {"Bowl" , "Plate" , "Cup" , "Knife"}

# utensils.add("Napkin")
# utensils.remove("Fork")
# utensils.clear() 
# utensils.update(dishes) - add to the list

dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))
print(utensils.intersection(dishes)) # in common 

for x in dinner_table:
    print(x , end = " , ")