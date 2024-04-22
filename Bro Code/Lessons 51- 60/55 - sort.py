# sort() method = used with lists
# sort() function = used with iterables

'''
students = ["Squidward" , "Sandy" , "Patrick" , "Spongebob" , "Mr.Krabs"]

students.sort(reverse = True) # key, reverse
sorted_students = sorted(students, reverse = True)


for i in sorted_students:
    print(i)
'''

'''
              # 0        # 1   # 2
students = [("Squidward", "F" , 60),
            ("Sandy" , "A" , 33),
            ("Patrick" , "D" , 36),
            ("Spongebob" , "B" , 20),
            ("Mr. Krabs" , "C" , 78)]

grade = lambda grades: grades[1]
students.sort(key = grade, reverse = True)

for i in students:
    print(i)
'''

              # 0        # 1   # 2
students = [("Squidward", "F" , 60),
            ("Sandy" , "A" , 33),
            ("Patrick" , "D" , 36),
            ("Spongebob" , "B" , 20),
            ("Mr. Krabs" , "C" , 78)]

ages = lambda ages: ages[2]
sorted_students = sorted(students, key = ages)

for i in sorted_students:
    print(i)

