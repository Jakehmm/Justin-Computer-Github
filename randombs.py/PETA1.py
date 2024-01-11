z = int(input("""
Salary Range:
0 - 10000
10001 - 30000
30001 - 70000
70001 - 140000
140001 - 250000 
250001 - 500000 
500001 - Above     
Enter Salary: """))
if z < 1000:
    print("Tax Rate: 5%")
elif z == 10001 < 30000:
    print("Tax Rate: 10%")
elif z == 30001 < 70000:
    print("Tax Rate: 15% ")
elif z == 70001 < 140000:
    print("Tax Rate: 20% ")
elif z == 140001 < 250000:
    print("Tax Rate: 25% ")
elif z == 250001 < 500000:
    print("Tax Rate: 30% ")
elif z == 500001 < z:
    print("Tax Rate: 35% ")
else:
    print("Please type a number")
    