# -*- coding: utf-8 -*-

from collections import defaultdict

def DFSUtil(graph,src,result,visited):
    visited[src] = True
    result.append(src)
    for i in graph[src]:
        if visited[i] == False:
            DFSUtil(graph,i,result,visited)
            
def DFS(src,graph,V):
    visited = [False]*V
    result = []
    DFSUtil(graph,src,result,visited)
    
    return result
if __name__ == "__main__":
    graph = defaultdict(list)
    graph[0] = [1,2,3]
    graph[1] = [3,4]
    graph[2] = [4]
    graph[3] = [4]
    graph[4] = []
    V = 5 # number of vertices
    print(DFS(0,graph,V))


