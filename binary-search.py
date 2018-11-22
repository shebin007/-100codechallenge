def binary_sort(sortedlist,n,x):
 
 start = 0
 end = n - 1

 while(start <= end):
  mid = (start + end)/2
  if (x == sortedlist[mid]):
   return mid
  elif(x < sortedlist[mid]):
   end = mid - 1
  else:
   start = mid + 1 
 
 return -1

n = input("Enter the size of the list: ")

