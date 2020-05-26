
class Solution:
    def findMaxLength(self, nums):
        if len(nums) == 0:
            return 0
        
        hm = {}
        subarr,count = 0,0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count -=1
            else :
                count +=1
            if count == 0:
                subarr = i + 1
            if count in hm:
                subarr = max(subarr,i - hm[count])
            else:
                hm[count] = i
        return subarr

if __name__ == "__main__":
    nums = [0,1,0]
    s = Solution ()
    print(s.findMaxLength(nums))