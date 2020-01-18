arr = [99,81,65,45,23,1,2,4]
print("Unsorted Array",arr)
def msort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        i=j=k= 0
        print("Splitting:",arr)
        
        msort(left)
        msort(right)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] =  right[j]
                j = j+1
            k = k + 1

        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            arr[k] = right[j]
            j = j + 1
            k = k + 1
        print("Merging:",arr)    

msort(arr)
print("Sorted Array",arr)
