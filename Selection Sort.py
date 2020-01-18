def selection(nums):
    for i in range(len(nums)):
        least=i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[least]:
                least=j
        swap(nums,least,i)
def swap(nums,x,y):
    temp=nums[x]
    nums[x]=nums[y]
    nums[y]=temp


nums=[9,8,3,5.5,7,6,4,0]
selection(nums)


print(nums)
