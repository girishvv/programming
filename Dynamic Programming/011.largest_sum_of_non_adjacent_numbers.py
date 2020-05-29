# -*- coding: utf-8 -*-

#For example, [2, 4, 6, 2, 5] should return 13, 
#since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#O(n) time and O(n) space

# 1. if an element is selected then the next element cant be selected
# 2. if an element is not selected then the next element can be selected
def largestSum(nums):
    n = len(nums)
    
    if n == 0:
        return None
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0],nums[1])
    
    dp = [0]*(n)
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    
    for i in range(2,n):
        dp[i] = max(nums[i]+dp[i-2],dp[i-1])
    
    return dp[-1]

def largestSum_const_space(nums):
    
    n = len(nums)
    
    if n == 0:
        return 0
    
    val1 = nums[0]
    if n ==1:
        return val1
    
    val2 = max(nums[0],nums[1])    
    if n == 2:
        return val2
    
    max_val = None
    
    for i in range(2,n):
        max_val = max(nums[i]+val1,val2)
        val1 = val2
        val2 = max_val
    return max_val
    
if __name__ == "__main__":
    nums = [2,4,6,2,5]
    print(largestSum(nums))
    print(largestSum_const_space(nums))


