from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,m1,m2 = list(map(int,input().strip().split()))
        edges_F = []
        edges_G = []
        
        for _ in range(m1):
            u,v = list(map(int,input().strip().split()))
            edges_F.append((u-1,v-1))

        for _ in range(m2):
            u,v = list(map(int,input().strip().split()))
            edges_G.append((u-1,v-1))

        parent_F = list(range(n))
        parent_G = list(range(n))
        rank_F = [0] * n
        rank_G = [0] * n

        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1

        for u,v in edges_G:union(parent_G,rank_G,u,v)
        
        add = remove = 0
        for u,v in edges_F:
            if find(parent_G,u) != find(parent_G,v):remove+= 1
            else:union(parent_F,rank_F,u,v)
        
        for u,v in edges_G:
            if find(parent_F,u) != find(parent_F,v):
                union(parent_F,rank_F,u,v)
                add+=1    
        return add+remove

if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    yes = "YES"
    no = "NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)