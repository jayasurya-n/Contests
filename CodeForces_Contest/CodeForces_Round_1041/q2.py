import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def run(self):
        n,pos = lii()
        s = si()
        pos-=1
        
        start1 = pos-1
        while(start1>=0 and s[start1]=='.'):start1-=1
        left = start1+1

        nleft = left if pos-1>=0 and s[pos-1]=='#' else pos

        start2 = pos+1
        while(start2<n and s[start2]=='.'):start2+=1
        right = n-start2

        nright = right if pos+1<n and s[pos+1]=='#' else n-pos-1

        return max(min(nleft,right),min(left,nright))+1



if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)