# -*- coding: utf-8 -*-
def find_min_steps(A,B,N):
    ind_a = 0
    ind_b = 0
    temp = float('inf')
    diff = []
    
    for i in range(N):
        if A[i] >= B[i] and temp > (A[i] - B[i]) :
            temp = A[i] - B[i]
            ind_a = i
            ind_b = i
    diff.append(A[ind_a])
    temp = A[ind_a] - B[ind_a]
    
    while True:        
        if temp > 0:
            diff.append(temp)
            temp = temp - B[ind_a]
        else:
            break
    #print(diff)
    ans = float('inf')
    C = [x for x in A]
    D = [x for x in B]
    #print(C,D)
    for i in range(len(diff)):
        item = diff[i]
        count = 0
        A = [x for x in C]
        B = [x for x in D]
        
        for j in range(N):
            if A[j] == item:
                continue
            else:
                if A[j] < B[j]:
                    print(-1)
                    return
                elif (A[j]-B[j])%item == 0:
                    count += (A[j]-B[j])//item
                elif B[j] == 1:
                    count += A[j]-item
                    
        if ans > count:
            ans = count     
    if ans == 0:
        print(-1)
    else:
        print(ans)
   
    
if __name__ == "__main__":
    N = 5
    A = [5, 7, 10, 5, 15]
    B = [2, 2, 1, 3, 5]
    
    N = 2
    A = [5,6]
    B = [4,3]
    
    find_min_steps(A,B,N)

