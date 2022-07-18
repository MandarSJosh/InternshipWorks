from array import * 

arr = array('u',[ 'a' , '-' , '*' ,])

for e in arr:
  print(e)

newArr = array(arr.typecode, [a for a in arr])

i = 0
while i<len(newArr):
  print(newArr[i])
  i += 1