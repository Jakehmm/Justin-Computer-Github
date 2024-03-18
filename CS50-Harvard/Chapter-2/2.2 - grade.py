score = int(input("Score: "))

if score >= 100:
    print("Perfect")
elif score >= 90:
    print("A+")
elif score >= 80:
    print("Average")
else:
    raise ValueError ("Stupid nigger")