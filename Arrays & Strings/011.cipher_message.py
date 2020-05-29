# -*- coding: utf-8 -*-

def cipher(word,k):
    word_list = [ch for ch in word]
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smalls = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    
    for i in range(len(word_list)):
        if word_list[i] in caps:
            index = caps.find(word_list[i])
            #print("Index",index)
            word_list[i] = caps[(index + k) %26]
        if word_list[i] in smalls:
            index = smalls.find(word_list[i])
            #print("Index",index)
            word_list[i] = smalls[(index + k) %26]
        if word_list[i] in nums:
            index = nums.find(word_list[i])
            print("Index",index)
            word_list[i] = nums[(index + k) %10]    
    
    print("".join(word_list))

if __name__ == "__main__":
    word = "All-convoYs-9-be:Alert1."
    k = 4
    cipher(word,k)

