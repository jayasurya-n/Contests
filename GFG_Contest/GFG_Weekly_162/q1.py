from typing import List,Optional
import sys
class Solution:
    
    def power(self,a,b):
        mod = 1000000007
        ans = 1
        while b:
            if(b%2==1):
                ans = (ans*a)%mod
                b-=1
            a = (a*a)%mod
            b=b//2
        return int(ans)

    def countWays(self, n : int) -> int:
        mod = 1000000007
        all = self.power(10,n-1)
        zero_7s = self.power(9,n-1)
        ans = ((all*9)%mod - (zero_7s*8)%mod)%mod
        return ans
    
    # def countWays(self, n : int) -> int:
    #     mod = 1000000007
    #     all = pow(10,n-1,mod)
    #     zero_7s = pow(9,n-1,mod)
    #     ans = ((all*9)%mod - (zero_7s*8)%mod)%mod
    #     return ans



# time complexity: O(logN)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n = int(input().strip())
        print(Solution().countWays(n))


