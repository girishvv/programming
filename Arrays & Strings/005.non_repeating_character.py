# -*- coding: utf-8 -*-

# Implement your function below.
def non_repeating(given_string):
    if len(given_string) == 0:
        print(None)
        return
    hm = {}
    
    for ch in given_string:
        if ch not in hm:
            hm[ch] = 1
        else:
            hm[ch] += 1
    
    for key in hm:
        if hm[key] == 1:
            print(key)
            return
    print(None)
    
    return None

if __name__ == "__main__":
    # NOTE: The following input values will be used for testing your solution.
    non_repeating("abcab") # should return 'c'
    non_repeating("abab") # should return None
    non_repeating("aabbbc") # should return 'c'
    non_repeating("aabbdbc") # should return 'd'

