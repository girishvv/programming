# -*- coding: utf-8 -*-
def selectionSort(nums):
    if len(nums) <= 1:
        return nums
    result = []
    for i in range(len(nums)):
        smallest = findSmallest(nums)
        result.append(nums.pop(smallest))
    return result

def findSmallest(nums):
    smallest = nums[0]
    index = 0
    for i in range(1,len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            index = i
    return index
            
if __name__ == "__main__":
    nums = [7,5,6,8,9,1,3,2,0]
    print(selectionSort(nums))

