# str.format() = optional method that gives users
# more control when displaying output
# basically fstring


animal = 'cow'
item = 'moon'

#print("The {} jumped over the {}".format(animal.item)) 
print("The {1} jumped over the {1}".format(animal,item)) # positional argument
print("The {item} jumped over the {animal}".format(animal = "cow" , item = "moon")) # keyword argument , can be reused { animal } {animal }

text = 'The {} jumped over the {}'
newtext = text.format(animal,item)
print(newtext)



name = "Bro"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))


pi = 3.14159

print("The number pi is {:.2f}".format(pi))

print(f'The number pi is {pi:.2f}')

number = 1000000

print(f'The number is {number:,}')
print(f'The number is {number:b}')
print(f'The number is {number:o}')
print(f'The number is {number:X}')
print(f'The number is {number:e}')