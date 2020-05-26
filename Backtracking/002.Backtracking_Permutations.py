# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:17:52 2020

@author: girishvv
"""
def permutations(inp,partial,used):
    if len(inp) == len(partial):
        print(partial)
    else:
        for i in range(0,len(inp)):
            if used[i]==False and not (inp[i]==inp[i-1] and not used[i-1]==False):
                used[i] = True
                partial.append(inp[i])
                permutations(inp,partial,used)
                used[i] = False
                partial.pop(len(partial)-1)
                
if __name__ == "__main__":
    inp = [1,2,2]
    used = [False]*(len(inp))
    permutations(inp,[],used)
