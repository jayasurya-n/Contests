from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,m = list(map(int,input().strip().split()))
        cards = []
        for i in range(n):
            temp = list(map(int,input().strip().split()))
            temp.sort()
            cards.append((temp,i+1))
        
        cards.sort(key=lambda x:x[0][0])
        for turn in range(m):
            for cow in range(n-1):
                if(cards[cow][0][turn]>cards[cow+1][0][turn]):return [-1]
            if(turn<m-1 and cards[-1][0][turn]>cards[0][0][turn+1]):return [-1]
        return [x[1] for x in cards]

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
        for num in ans:
            print(num,end=" ")
        print()