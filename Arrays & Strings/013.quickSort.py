# -*- coding: utf-8 -*-
import random

#picks pivot at random index
def findPivot(nums):
    i = random.randrange(0,len(nums))
    nums[i],nums[0] = nums[0],nums[i]
    return nums[0]

def quickSort(nums):
    if len(nums) < 2:
        return nums
    else:
        pivot = findPivot(nums)
        less = [i for i in nums[1:] if i <= pivot]
        greater = [i for i in nums[1:] if i > pivot]
        
        return quickSort(less) + [pivot] + quickSort(greater)

if __name__ == "__main__":
    nums = [9,2,3,4,5,1,6,7,0]
    print(quickSort(nums))

