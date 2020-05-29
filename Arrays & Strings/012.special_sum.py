# -*- coding: utf-8 -*-

def special_sum(N,data):
    
    total = float('-inf')
    series = [0]*(N)
    for i in range(1,N):
        series[i] = series[i-1]+1
    print(series)
    k = 1
    for i in range(N):
        k = 1
        j = i + 1
        temp = 0
        while j < N+1:
            temp += sum(data[i:j])
            #print(data[i:j])
            i = i + series[k]
            j = j + series[k+1]
            k += 1
        if temp > total:
            total = temp            
    print(total)
            

if __name__ == "__main__":
    
    N = 10
    data = [2, 1, 3, 9, 2, 4, -10, -9, 1, 3]

    print(special_sum(N,data))
