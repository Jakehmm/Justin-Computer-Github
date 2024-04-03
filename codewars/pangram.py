alphabet = 'abcdefghijklmnopqrstuvwxyz'


def is_pangram(s):
   for letters in alphabet:
      if letters not in s.lower():
         return False
   return True
