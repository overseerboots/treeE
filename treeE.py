from os import walk
import sys

# Functions #####################################
def print_help():
    print("help coming soon™")

def print_files(f):
    file_extension = f.split(".")
    file_extension = file_extension[len(file_extension) - 1]
    if file_extension == "mp4": # .mp4
        print("└──","\U000f022b",f)
    elif file_extension == "txt": # .txt
        print("└──","\U0000f15c",f)
    elif file_extension == "md": # .md
        print("└──","\U0000f48a",f)
    elif file_extension == "py": # .py
        print("└──","\U0000e73c",f)
    else:
        print("└──","\U000f086f",f)

#################################################

try:
    path = sys.argv[1]
except:
    path = sys.argv[0]

items = []

if path == "--help":
    print_help()


for (root, dirs, file) in walk(path):
    dir_name = path.split("/")
    dir_name = dir_name[len(dir_name)-2]
    print("\U0000e5ff",dir_name)
    for f in file:
        print_files(f)