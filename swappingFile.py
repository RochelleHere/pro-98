def swapFileData():
  with open("sample1.txt", "r") as a:
    data_a = a.read()
  with open("sample2.txt", "r") as b:
    data_b = b.read()
  with open("sample1.txt","w") as a:
    a.write(data_b)
  with open("sample2.txt","w") as b:
    b.write(data_a)

swapFileData()















#  #   Define a swapFileData function using def
# #Use inputs to take the names of the files to swap.
# #Open file1 and read it’s data and save it in a variable called data_a.
# #Open file2 and read its data and save it in a variable called data_b.
# Open file 1 in writing mode and write data_b to it.
# Open file 2 in writing mode and write data_a to it.
# Call the function.
# Save the code.