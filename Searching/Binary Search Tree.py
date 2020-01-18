def binary(arr,value,low,high,n):
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1        


arr = [9,88,7,65,55,44,88,1,4]
arr.sort()
print(arr)
n = len(arr)
value = int(input("ENter element :"))
result = binary(arr,value,0,n-1,n)
if result == -1:
    print ("Element is not present")
else:
    print("Element is present at index:",result)
