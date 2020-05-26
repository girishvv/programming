# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:11:42 2020

@author: girishvv
"""
# Implement your function below.
def most_frequent(given_list):
    max_item = -1
    result = None
    hm = {}
    for element in given_list:
        if element not in hm:
            hm[element] = 1
        else:
            hm[element] += 1
    #for element in given_list:
        if hm[element] > max_item:
            max_item = hm[element]
            result = element
            
    return result


if __name__== "__main__":
    # NOTE: The following input values will be used for testing your solution.
    # most_frequent(list1) should return 1
    list1 = [1, 3, 1, 3, 2, 1]
    print(most_frequent(list1))
    # most_frequent(list2) should return 3
    list2 = [3, 3, 1, 3, 2, 1]
    print(most_frequent(list2))
    # most_frequent(list3) should return None
    list3 = []
    print(most_frequent(list3))
    # most_frequent(list4) should return 0
    list4 = [0]
    print(most_frequent(list4))
    # most_frequent(list5) should return -1
    list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]    
    print(most_frequent(list5))