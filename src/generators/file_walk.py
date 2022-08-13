import os
root = 'music'

for path, directory, files in os.walk(root, topdown=True):
    print(path)
    print(directory)
    print(files)
    input()
