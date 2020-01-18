def search(arr,value,n):
    for i in  range(0,n):
        if value == arr[i]:
            return i
    return -1    



arr = [5,14,8,22,9,44,90,1]
n = len(arr)
value = int(input("Enter the element to be searched : "))
result = search(arr,value,n)
if result == -1:
    print("Element is not found. Try another element")
else:
    print("Element is present at index",result)
    
