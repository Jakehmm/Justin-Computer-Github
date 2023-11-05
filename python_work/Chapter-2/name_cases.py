person_name = "Eric"
print(f"Hello {person_name}, would you like to learn some python today")

name_kind = "Eric"
print(f"{name_kind.title()}")
print(f"{name_kind.upper()}")
print(f"{name_kind.lower()}")

#if u wanna do double quotations then use 'single quotations' not "double quotations"
# I just did stringing them but this is basic
quote_name = '"Imagination is the highest form of research"'
print(f"I once said, {quote_name}")

# Double string, just understand (me)
famous_person = "Albert Einstein once said,"
message = '"Imagination is the highest form of research."'
print(f"{famous_person} {message}")

# This is supposedly to add Whitespaces I guess, dont fucking understand the point for this, but yeah you get the point
ws_name = ' Felippe '
print("\t" + ws_name)

ws_name = ' Felippe '
print("\n" + ws_name)

# This basically just removes the spaces on the left
jon_names = '                               " jon porieori "'
print(jon_names.lstrip())


# This basically just removes the spaces on the right 
#for the rstrip I dont get it, I dont see the difference tF?
dog_names = '" hushppy "          d  '
print(dog_names.rstrip())

# For this is just removes the beginning and the end
basic_name = "                    Justin                                "
print(basic_name.strip())


