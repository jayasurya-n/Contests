import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def run(self):
        n = ii()
        s = si()

        if(n<=3):return n
        ans = 3
        for i in range(n-3):
            if(s[i:i+4]=='1010' or s[i:i+4]=='0101'):
                ans = 4
                break
        
        ones = zeros = 0
        i = 0
        for j in range(n):
            if(s[j]=='1'):ones+=1
            else:zeros+=1

            while i<j and zeros>1:
                if(s[i]=='1'):ones-=1
                else:zeros-=1
                i+=1
            
            ans = max(ans,j-i+1)

        ones = zeros = 0
        i = 0
        for j in range(n):
            if(s[j]=='1'):ones+=1
            else:zeros+=1

            while i<j and ones>1:
                if(s[i]=='1'):ones-=1
                else:zeros-=1
                i+=1
            
            ans = max(ans,j-i+1)
        
        return ans
    


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)