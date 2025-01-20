from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n,x = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))

        ans = 0
        required = []
        
        extra = 0
        for i in range(n):
            if(arr[i]>=x):
                extra+=arr[i]-x
                ans+=1
            else:
                required.append(x-arr[i])
        
        required.sort()

        for i in range(len(required)):
            if(extra>=required[i]):
                extra-=required[i]
                ans+=1
            else:break
        return ans



# time complexity: O(nlogn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())