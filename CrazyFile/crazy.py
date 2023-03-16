import os
import fnmatch

#put here your starter folder
folder = r'./tmp/'

count=1
old_name=[]
new_name=[]
f1 = open("list_oldfile.txt", "w")
f2 = open("list_newfile.txt", "w")
# iterate all files from a directory

for root, dirs, files in os.walk(folder):
    for file_name in files:
        if fnmatch.fnmatch(file_name, "*.txt") or fnmatch.fnmatch(file_name, "*.pdf"):
            # construct old file name
            source = os.path.join(root, file_name)

            old_name.append(source)
            f1.write(source+"\n")

            file_name2="crazy_" + str(count) + ".gpan"
            destination = os.path.join(root, file_name2)

            new_name.append(destination)
            f2.write(destination + "\n")

            print(source)
            print(destination)
            os.rename(source, destination)
            count += 1


f1.close()
f2.close()


