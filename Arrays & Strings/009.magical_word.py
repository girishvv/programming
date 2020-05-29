# -*- coding: utf-8 -*-
def findNearest(n,prime_nums):
    if n <= prime_nums[0]:
        return prime_nums[0]
    if n >= prime_nums[-1]:
        return prime_nums[-1]
    
    i = 0
    
    while(n > prime_nums[i]):
        i +=1
    if abs(n-prime_nums[i]) < abs(n-prime_nums[i-1]):
        return prime_nums[i]
    elif abs(n-prime_nums[i]) == abs(n-prime_nums[i-1]):
        return prime_nums[i-1]
    else:
        return prime_nums[i-1]
        
def magicalWord(S):
    print(ord('a'),chr(65))
    print(ord('z'))
    #prime numbers between 65 and 90
    prime_caps = [67,71,73,79,83,89]
    prime_small = [97,101,103,107,109,113]
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smalls = "abcdefghijklmnopqrstuvwxyz"
    #word_ascii = [ord(ch) for ch in S]
    #print(word_ascii)
    result = ""
    i = 0
    for ch in S:
        if ch in caps:
            temp = findNearest(ord(ch),prime_caps)
        elif ch in smalls:
            temp = findNearest(ord(ch),prime_small)
        else:
            temp = prime_caps[0]
        
        #temp = findNearest(n,prime_caps)
        result += chr(int(temp))
        i += 1
    
    print("".join(result))
    
    
if __name__ == "__main__":
    S = "j4eZamQY0SQgM9cX7dcb"
    magicalWord(S)
