# -*- coding: utf-8 -*-

# Implement your function below.
def common_elements(list1, list2):
    result = []
    
    if len(list1) == 0 or len(list2) == 0:
        return result
    m = len(list1)
    n = len(list2)
    i,j = 0,0
    while(i<m and j<n):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i +=1
            j +=1
            
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
            
    return result



if __name__ == "__main__":
    # NOTE: The following input values will be used for testing your solution.
    list_a1 = [1, 3, 4, 6, 7, 9]
    list_a2 = [1, 2, 4, 5, 9, 10]
    # common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).
    print(common_elements(list_a1, list_a2))
    list_b1 = [1, 2, 9, 10, 11, 12]
    list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
    # common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).
    print(common_elements(list_b1, list_b2))
    list_c1 = [0, 1, 2, 3, 4, 5]
    list_c2 = [6, 7, 8, 9, 10, 11]
    # common_elements(list_b1, list_b2) should return [] (an empty list).
    print(common_elements(list_c1, list_c2))
    