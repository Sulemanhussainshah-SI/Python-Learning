import os

# Directory to list (change this to any path you want)
directory = "/Program Files" 


try:
    contents = os.listdir(directory)#list all files and directory in the specified path

    print(f"Contents of '{directory}':")#print each files and directory
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Directory not found.")
except PermissionError:
    print("Permission denied.")