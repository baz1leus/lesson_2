def Sort(List):
  
  List.sort()
  
  return(List)

List = [1, 0, 2]

print(Sort(List))

def sort_bubble(arr):
    n = len(arr)
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

from random import randint
list = [randint(1, 111) for i in range(10)]

print(*sort_bubble(list))
