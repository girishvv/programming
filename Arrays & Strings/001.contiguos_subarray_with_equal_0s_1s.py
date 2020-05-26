
# consider 0 as -1 and keep couting until count become 0
# diffrence between indexes of last 0 seen and first 0 seen is the answer
# dictionary is used to track the indices of count 0 seen

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
            # if sum is 0, then note that index and add it to the
            # dictionary if not already present in dict
            # if present in dict then update the result with the diff of current  0 index
            # and last seen 0 index
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
