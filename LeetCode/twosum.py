def fun(nums,target):
    low,high = 0,len(nums)-1
    while (low < high):
        sum = nums[low] + nums[high]
        if sum == target:
            return [low,high]
        elif sum < target:
            low += 1
        else:
            high -= 1

print(fun([3,2,4],6))