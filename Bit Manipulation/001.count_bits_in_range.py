# -*- coding: utf-8 -*-
#Given a non negative integer number num. 
#For every numbers i in the range 0 ≤ i ≤ num 
#calculate the number of 1's in their binary representation and return them as an array.
#Input: 5
#Output: [0,1,1,2,1,2]

class Solution:
    def countBits(self, num):
        ans = [0]*(num+1)
        
        ans[0] = 0

        for i in range(1,num+1):
           ans[i] = ans[i >> 1] + (i & 1)
        return ans
              
           
        
        
if __name__ == "__main__":
    n = 1
    s = Solution()
    print(s.countBits(n))