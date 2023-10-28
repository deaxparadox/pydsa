import os

files_dir = "/home/creator/Documents/Paradox/Github/DSA/Python/files"

files = os.listdir(files_dir)

class F:
    ...

f = F()
for file in files:
    setattr(f, f"{file}", os.path.join(files_dir, file))
    # print(file)


print(getattr(f, "words_list.txt"))