import random

dice = random.randint(1,6)
dice_float = random.random()

mylist = ['rock' , 'paper' , 'scissors']
z = random.choice(mylist)

cards = [1,2,3,4,5,6,7,8,9, "Jack" , "Queen" , "King"]
random.shuffle(cards)

print(z)
print(dice)
print(cards)
