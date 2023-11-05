# the pop() basically removes the last

personality_trait = ['sad' , 'grief' , 'bean' , 'toasted']
traits = personality_trait.pop(0) # <--- for the parenthesis you can assign to which u want to pop , either (0,1,2,3)
# If parenthesis is left blank it will auto pop last one, pretty fun command
print(f"I was {traits.title()} yesterday")

# If you want to delete an item from a list and not use that item in anyway, 
# use the del statement; if you want to use an item as you remove it, use the pop method

