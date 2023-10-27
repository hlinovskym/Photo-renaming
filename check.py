import os

PATH = "/.../"

files = os.listdir(PATH)
length = []

for file in files:
    length.append(len(file))

print(len(files))
print(len(length))
print(min(length))
print(max(length))
