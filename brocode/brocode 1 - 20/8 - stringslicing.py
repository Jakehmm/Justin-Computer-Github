# Slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]
# Inclusive - Exclusive

# Indexing
name = "Justin Wu"

first_name = name[:]
last_name = name[4:8]
funky_name = name[0:8:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# Slicing

website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) # Three values also , [start:stop:step] they seperate with comma

print(website[slice])
print(website2[slice])

