from array import *

arr = array('i', [])
n = int(input("Enter the length of the array: "))

for i in range(n):
  x = int(input('Enter the next value: '))
  arr.append(x)

for i in range(n):
  print(arr[i])

val = int(input("Enter the value for search of indexation: "))
k = 0

for e in arr:
  if e == val:
    print(k)
    break

  k += 1
  
else:
    print("Invalid input.")    
  