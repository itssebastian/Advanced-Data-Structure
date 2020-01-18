def search(arr,value,n):
    for i in  range(0,n):
        if value == arr[i]:
            return i
        elif value < arr[i]:
            return -1



arr = [6,18,4,22,78,44,90,1,3]
arr.sort()
print (arr)
n = len(arr)
value = int(input("Enter the element to be searched : "))
result = search(arr,value,n)
if result == -1:
    print("Element is not found. Try another element")
else:
    print("Element is present at index",result)
    
