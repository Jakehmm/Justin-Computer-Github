a  = "$$$$$$\n"
a += "   $\n"
a += "   $\n"
a += "   $\n"
a += "   $\n"
a += "$$$$"

my_name = "Apple"  # gets from input
my_name = my_name.lower()  # so we check both a and A together

if my_name.startswith("a"):
    print(a)

b = (
    "@@@@\n"
    "  @\n"
    "  @\n"
    "  @\n"
    "@@@"
)
print(b)

print(f"{b}\n")

symbols = {
    "a": ("@@@@\n"
          "  @\n"
          "@@@\n"),
          
          
    "b": ("@@@@ \n"
          "  @\n"
          "  @ \n"
          "  @\n"
          "@@@"),
}

sample_letter = "a"
print( symbols.get(sample_letter, " ") )

sample_letter = "b"
print( symbols.get(sample_letter, " ") )

'''
this simply says
dict_ = {
    "key that exists": "value",
}

print(dict_.get("key that exists", "something else"))
print(dict_.get("nonexistent key", "default value"))
'''