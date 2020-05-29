# -*- coding: utf-8 -*-

def findMax(s):

    hm = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
    sticks = 0
    result = []
    for ch in s:
       sticks+= hm[int(ch)] 
    i = 0
    if sticks %2 == 0:
        while i < (sticks//2):
            result.append("1")
            i +=1
    else:
        result.append("7")
        while i < ((sticks-3)//2):
            result.append("1")
            i +=1
    
    return "".join(result)         


if __name__ == "__main__":
    print(findMax("02"))


