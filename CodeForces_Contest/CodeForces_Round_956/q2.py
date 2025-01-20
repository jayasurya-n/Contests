from typing import List,Optional
import sys
class Solution:
    def func(self,a,b,n,m) -> Optional[int]:
        for i in range(n):
            sum_a,sum_b=0,0
            for j in range(m):
                sum_a+=a[i][j]
                sum_b+=b[i][j]
            sum_a%=3
            sum_b%=3
            if(sum_a!=sum_b):return "NO"
        
        for j in range(m):
            sum_a,sum_b=0,0
            for i in range(n):
                sum_a+=a[i][j]
                sum_b+=b[i][j]
            sum_a%=3
            sum_b%=3
            if(sum_a!=sum_b):return "NO"
        
        return "YES"





# time complexity: O(n^2)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n,m = list(map(int,input().strip().split()))
        a,b = [],[]
        for i in range(n):
            a.append([int(i) for i in input().strip()])

        for i in range(n):
            b.append([int(i) for i in input().strip()])
        # print(a,b)
        print(Solution().func(a,b,n,m))