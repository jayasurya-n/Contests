from typing import List,Optional
import sys
class Solution:

    def maximumSum(self, n : int, k : int) -> int:
        is_prime = [True]*(n+1)
        i = 2
        while(i<=n):
            if(is_prime[i]==True):
                for j in range(2*i,n+1,i):
                    is_prime[j] = False
            i+=1
        ans = 0

        for i in range(n,0,-1):
            if(i%2==1):
                if(i==1 or is_prime[i]==False):
                    ans+=i
                    k-=1
                    if(k==0):return ans
        return -1
        


# time complexity: O(nlog(log(n)))
# space complexity: O(1)

t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n,k = list(map(int,input().strip().split()))
        print(Solution().maximumSum(n,k))