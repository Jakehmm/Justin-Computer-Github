# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metaata ( file's creation and modification times)


import shutil

# shutil.copyfile('test.txt','C:\Users\Justin Wu\OneDrive\Desktop\\copy.txt')
shutil.copyfile('test.txt' , 'copytext.txt') #source, destination
