def bubblesort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1,0,-1):
            if nums[j] < nums[j-1]:
                swap(nums,j,j-1)
def swap(nums,x,y):
    temp=nums[x]
    nums[x]=nums[y]
    nums[y]=temp

nums=[3,2,1,5,4,6,9,8,7]
bubblesort(nums)


print(nums)
