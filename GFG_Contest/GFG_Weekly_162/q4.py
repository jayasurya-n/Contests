from typing import List,Optional
import sys
class Solution:
    def countNumbers(self, L : int, R : int) -> int:
        sum = 0
        str_L = str(L)
        for i in range(len(str_L)):
            sum+=int(str_L[i])
        # return sum
        
        ans = 0
        for i in range(L,R+1):
            digits = len(str(i))
            if(sum%digits==0):ans+=1
            sum+=1
        return ans




# time complexity: O()
# space complexity: O()
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        l,r = list(map(int,input().strip().split()))
        print(Solution().countNumbers(l,r))   