# -*- coding: utf-8 -*-
from collections import defaultdict 

class Solution:
    def canFinish(self, numCourses, prerequisites):

        g= Graph(numCourses)
        
        for i in range(len(prerequisites)):
            g.addEdge(prerequisites[i][0],prerequisites[i][1]); 

        if g.isCyclic() :
            return False
        else:
            return True
        
class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def isCyclicUtil(self, v, visited, recStack): 
  
        visited[v] = True
        recStack[v] = True

        for neighbour in self.graph[v]: 
            if visited[neighbour] == False: 
                if self.isCyclicUtil(neighbour, visited, recStack) == True: 
                    return True
            elif recStack[neighbour] == True: 
                return True
        recStack[v] = False
        return False
  
    def isCyclic(self): 
        visited = [False] * self.V 
        recStack = [False] * self.V 
        for node in range(self.V): 
            if visited[node] == False: 
                if self.isCyclicUtil(node,visited,recStack) == True: 
                    return True
        return False
    
if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(0,[]))
  


