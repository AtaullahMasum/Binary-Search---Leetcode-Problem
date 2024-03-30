def lowerBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    floor = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= x:
            floor = mid
            high = mid -1 
        else:
            low = mid + 1
    return floor

    