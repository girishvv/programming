# -*- coding: utf-8 -*-
class Solution:
    def minDistance(self, word1,word2):
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        
        DP = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if i == 0:
                    DP[0][j] = j
                if j== 0:
                    DP[i][0] = i
                elif word1[i-1] == word2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = 1 + min(DP[i-1][j],DP[i][j-1],DP[i-1][j-1])
        return DP[len(word1)][len(word2)]
        
if __name__ == "__main__":
    word1 = "sea"
    word2 = "ate"
    s = Solution()
    print(s.minDistance(word1,word2))

