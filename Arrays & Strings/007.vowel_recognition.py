# -*- coding: utf-8 -*-
def countVowels(s):
    v = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in v:
            count +=1
    return count
    
def subString(s, n): 
    # Pick starting point in outer loop 
    # and lengths of different strings for 
    # a given starting point 
    count = 0
    for i in range(n): 
        for len in range(i+1,n+1): 
            print(s[i: len]) 
            count += countVowels(s[i: len])
    return count

#choose(input_list=[1, 2, 3, 4, 5], k=3)
if __name__ == "__main__":
    s = "xux"
    data = [ch for ch in s]
    
    print(subString(data,3))
    

