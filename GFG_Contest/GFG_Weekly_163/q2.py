from typing import List,Optional
import sys
class Solution:
    def CountString(self,x,y):

        if(x>y+1):return 0
        
        # (y+1) C x
        mod = 10**9+7
        y = y+1
        if(y>2*x):x = y-x
        ans=1
        for i in range(x):
            ans= (ans*(y-i))%mod
            ans= (ans*pow(i+1,mod-2,mod))%mod
        return int(ans)





# time complexity: O(y)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        x,y = list(map(int,input().strip().split()))
        print(Solution().CountString(x,y))