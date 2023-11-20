brackets = ['I' , 'Am' , 'So', 'Lazy' , 'to', 'do', 'shit']
brackets.sort(reverse = True)
brackets.pop(0)
brackets.remove('I')

for value in range(0,10):
    brackets.append(value)
print(brackets)

name = ['Xavier', 'Jake', 'Seco', 'Everyone']
for names in name:
    print(f'{names} is gay')