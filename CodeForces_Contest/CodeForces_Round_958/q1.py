from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n,k = list(map(int,input().strip().split()))
        if(k==2):return n-1
        ans = n//(k-1)
        rem = n%(k-1)

        if(rem==0 or rem==1):return ans
        else:return ans+1




# time complexity: O(1)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())