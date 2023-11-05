guest_list = ['A' , 'B' , 'C' , 'D' , 'E' , 'F']
message = "Hey guys, I'm sorry we won't be having enough tables"
print(message)

A = guest_list.pop(0)
messageA = "I'm extremly sorry"
print(f'{messageA}, {A}')

B = guest_list.pop(0)
messageB = "I'm extremly sorry"
print(f'{messageB}, {B}')

C = guest_list.pop(0)
messageC = "I'm extremly sorry"
print(f'{messageC}, {C}')

D = guest_list.pop(0)
messageD = "I'm extremly sorry"
print(f'{messageD}, {D}')

message1 = f'{guest_list[0]}, {guest_list[1]}'
print(f'Hey, {message1}, I wanted to let you both know, you guys are still invited!')

del guest_list[0]
del guest_list[0]
print()


