# tuple = collection which is ordered and unchangeable
# used to group together related data

students = ("Bro",21,"Male")

print(students.count("Bro"))
print(students.index("Male"))

for x in students:
    print(x, end = ",")

if "Bro" in students:
    print("Bro is gaY!")