import os
import shutil

path = 'gay'

try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError as e:
    print("That file was not found")
except PermissionError:
    print("You do not have permision to delete that")
except OSError:
    print("You cannot delete that")
else:
    print(path + " Was deleted")