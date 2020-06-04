# -*- coding: utf-8 -*-
from collections import deque 
from collections import defaultdict

def BFS(src,dst,graph):
    queue = deque()
    queue += graph[src]
    
    while queue:
        temp = queue.popleft()
        if temp == dst:
            return True
        else:
            queue +=graph[temp]
            
    return False

def BFS_Traversal(src,graph,V):
    
    visited = [False]*V
    queue = deque()
    
    queue.append(src)
    visited[src] = True
    result = []
    
    while queue:
        temp = queue.popleft()
        result.append(temp)
        for i in graph[temp]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return result
                
if __name__ == "__main__":
    graph = defaultdict(list)
    graph[0] = [1,2,3]
    graph[1] = [3,4]
    graph[2] = [4]
    graph[3] = [4]
    graph[4] = []
    
    
    src = 0
    dst = 0
    print(BFS(src,dst,graph))
    print(BFS_Traversal(0,graph,5))
