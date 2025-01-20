from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        self.longest_paths = []
        self.min_length = 0
        adj = [[] for _ in range(n)]
        
        for u,v,l in edges:
            adj[u].append((v,l))
        
        def dfs(u,parent,length,nodes,values):
            for v,l in adj[u]:
                if(v!=parent and nums[v] not in values):
                    values.add(nums[v])
                    nodes+=1
                    length+=l
                    if(length>self.min_length):
                        self.min_length = length
                        self.longest_paths = [(length,nodes)]
                    elif(length==self.min_length):self.longest_paths.append((length,nodes))
                    dfs(v,u,length,nodes,values)
                    values.remove(nums[v])
                    nodes-=1
                    length-=l
        
        for u in range(n):dfs(u,-1,0,1,{nums[u]})
        if(not self.longest_paths):return [0,1]
        return [self.longest_paths[0][0],min(nodes for _,nodes in self.longest_paths)]
        
# time complexity: O()
# space complexity: O()©leetcode
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))