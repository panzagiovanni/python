import os

# opening the file in read mode
f1 = open("lista_oldfile.txt", "r")
f2 = open("lista_newfile.txt", "r")

# reading the file
data1 = f1.read()
data2 = f2.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list1 = data1.split("\n")
data_into_list2 = data2.split("\n")

for i in range(len(data_into_list1)):
  print(data_into_list2[i])
  print(data_into_list1[i])
  os.rename(data_into_list2[i], data_into_list1[i])


print(data_into_list1)
f1.close()
f2.close()
