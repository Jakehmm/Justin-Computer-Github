# dictionary = A changable, unordered collection of unique key:value
# pairs. Fast because they use hashing, allow us to access a value
# quickly

capitals = {'USA': 'Washington DC' , 
            'Philippines': 'Manila',
            'Russia':'Moscow'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Los Angeles'})
capitals.pop('USA')
capitals.clear()

# print(capitals.get('Russia'))
# print(capitals.keys()) # print all keys
# print(capitals.values()) # print all value
# print(capitals.items()) # both all

for key,value in capitals.items():
    print(key,value)