numberX=int(input("enter the no of numbers:"))

i = 0
my_input = []
while i < numberX:
  numberY = int(input('enter the {} no :'.format(i)))
  my_input.append(numberY)
  print(my_input)
  i += 1
print(my_input)
def numpy(my_arr):
  print("inside function")
  print(my_arr)
  total=sum(my_arr)
  print("sum of the array is",total)

numpy(my_input)



