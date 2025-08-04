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
        
        def ask2(i1,i2,open,close):
            print('?',6,open,i1,i2,close,open,close)
            sys.stdout.flush()
            return ii()

        def ask1(start,end):
            queries = list(range(start,end+1)) 
            print('?',len(queries),*queries)
            sys.stdout.flush()
            return ii()

        low,high = 1,n
        if(ask1(1,n)==0):
            open = n
            close = 1
        else:
            while low<=high:
                mid = (low+high)//2
                if(ask1(1,mid)>=1):high = mid-1
                else:low = mid+1
            
            open = low-1
            close = low

        ans = [None]*n
        for i in range(1,n+1,2):
            if(i==n):
                val = ask2(i,i,open,close)
                if(val==3):ans[i-1] = '('
                else:ans[i-1] = ')'
            else: 
                val = ask2(i,i+1,open,close)
                if(val==6):  ans[i-1],ans[i] = ')','('            
                elif(val==4):ans[i-1],ans[i] = '(',')'   
                elif(val==3):ans[i-1],ans[i] = '(','('            
                elif(val==2):ans[i-1],ans[i] = ')',')'
        
        print('!',"".join(ans))
        sys.stdout.flush()
    
if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()