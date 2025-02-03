from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
            
        ans = [0,1]
        def dfs(start,end,u,parent,pathLength:List):
            for v,w in adj[u]:
                if(v==parent):continue
                nstart,nend = start,end+1
                last_index = hash[nums[v]]
                if(last_index>=nstart):nstart = last_index+1
                hash[nums[v]] = nend
                
                curr_length = w+pathLength[-1]-pathLength[nstart] if nstart<nend else 0
                if(curr_length>ans[0]):
                    ans[0] = curr_length
                    ans[1] = nend-nstart+1
                elif(curr_length==ans[0]):
                    ans[1] = min(ans[1],nend-nstart+1)
                
                pathLength.append(pathLength[-1]+w)
                dfs(nstart,nend,v,u,pathLength)
                pathLength.pop()
                hash[nums[v]] = last_index
        
        hash = defaultdict(lambda:-1)
        hash[nums[0]] = 0
        dfs(start=0,end=0,u=0,parent=-1,pathLength=[0])
        return ans
            
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))