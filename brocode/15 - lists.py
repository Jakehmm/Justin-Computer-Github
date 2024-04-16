# list = used to store multiple items in a single variable

food = ['pizza','hamburger','hotdog','spaghetti','pudding']

food[0] = 'sushi'

food.append('Carbonara') # add on last
food.remove("hotdog") # dead
food.pop() # pop last , still stored
food.insert(0,"cake") # insert
food.sort() # sort alpha
food.clear() # remove all elements

for x in food:
    print(x, end=' , ')