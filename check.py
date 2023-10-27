import os

PATH = "/__foto/2023/2023-01-01 - Matýsek a Verunka/sam/"

files = os.listdir(PATH)
length = []

for file in files:
    length.append(len(file))

print(len(files))
print(len(length))
print(min(length))
print(max(length))
