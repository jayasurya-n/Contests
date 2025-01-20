from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        q = int(input().strip())
        offset = 0
        snakes = deque([])
        for _ in range(q):
            query = input().strip()
            if(len(query)==1):
                _,length = snakes.popleft()
                offset+=length 
            else:
                if(query[0]=='1'):
                    length  = int(query[2:])
                    if(not snakes):snakes.append([0,length])
                    else:
                        last_head,last_length = snakes[-1]
                        snakes.append([last_head+last_length,length])
                elif(query[0]=='3'):
                    k = int(query[2:])
                    print(snakes[k-1][0]-offset)
                
if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    yes = "YES"
    no = "NO"
    for _ in range(1):
        Solution().run()