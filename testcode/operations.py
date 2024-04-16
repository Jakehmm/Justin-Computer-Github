import time

print('''You have 10 seconds to prepare! Get Ready''')

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("START!")