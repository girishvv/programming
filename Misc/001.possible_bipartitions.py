# -*- coding: utf-8 -*-
#Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
#Output: true
#Explanation: group1 [1,4], group2 [2,3]

import collections

class Solution:
    def possibleBipartition(self, N,dislikes):

        if len(data) == 1:
            if data[0][0]!=data[0][1]:
                return True
            else:
                return False
        hm = collections.defaultdict(list)
        
        for x in data:
            if x[0] not in hm[x[1]]:
                hm[x[1]].append(x[0])
                hm[x[0]].append(x[1])
        
        seen = {}
        stack = []
        
        for i in range(1,N+1):
            if i not in seen:
                seen[i] = 0
                stack = [i]
                while stack:
                    d = stack.pop()
                    if d in hm:
                        for a in hm[d]:
                            if a in seen:
                                if seen[d] == seen[a]:
                                    return False
                            else:
                                seen[a] = (seen[d]+1)%2
                                stack.append(a)
        return True
        
        print(hm)
    
if __name__ == "__main__":
    data = [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]
    N = 10
    s = Solution()
    print(s.possibleBipartition(N,data))


