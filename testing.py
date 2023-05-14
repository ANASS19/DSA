nums=[3,3]
target=6
def tosum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]!=nums[j]:
                if nums[i] + nums[j]==target:
                    return ([i,j])



print(tosum(nums,target))