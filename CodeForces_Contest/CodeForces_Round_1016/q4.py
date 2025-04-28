from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n = ii()
        q = ii()
        
        def findIndex(i,j,n,num):
            if(n==0):return [i,j]
            
            half = 1<<(n-1)
            size = 1<<(2*(n-1))
            
            if(0<num<=size):return findIndex(i,j,n-1,num)
            elif(size<num<=2*size):return findIndex(i+half,j+half,n-1,num-size)
            elif(2*size<num<=3*size):return findIndex(i+half,j,n-1,num-2*size)
            else:return findIndex(i,j+half,n-1,num-3*size)
        
        def findNum(i,j,n,start):
            if(n==0):return start
            
            half = 1<<(n-1)
            size = 1<<(2*(n-1))
            
            if(0<i<=half):
                #top-left
                if(0<j<=half):return findNum(i,j,n-1,start)
                
                #top-right
                else:return findNum(i,j-half,n-1,start+3*size)
            
            else:
                #bot-left
                if(0<j<=half):return findNum(i-half,j,n-1,start+2*size)
                
                #bot-right
                else: return findNum(i-half,j-half,n-1,start+size)
            
            
        for _ in range(q):
            query = lsi()
            if(query[0]=='->'):
                i,j = int(query[1]),int(query[2])
                print(findNum(i,j,n,1))
            else:
                num = int(query[1])
                ans = findIndex(1,1,n,num)
                print(*ans)
            

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()