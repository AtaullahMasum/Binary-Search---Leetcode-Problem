def floorAndCeil(arr, x):
  low , high = 0, len(arr)-1
  floor, ceil = -1, -1
  while low <= high:
    mid = (low + high)//2
    if arr[mid] == x:
      return arr[mid], arr[mid]
    elif arr[mid] > x: # lower bound 
      ceil = arr[mid]
      high = mid - 1
    else:
      floor = arr[mid]
      low = mid + 1
  return floor, ceil