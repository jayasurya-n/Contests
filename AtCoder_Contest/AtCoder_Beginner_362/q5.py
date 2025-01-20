from typing import List,Optional
import sys
class Solution:
    def countSubsequnce(self,arr,k):
        n = len(arr)
        dp = [{} for _ in range(n)]
        count = 0

    def run(self) -> Optional[list]:
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        ans = []
        ans.append(n)
        ans.append((n*(n-1))//2)

        for k in range(3,n+1):
            ans.append(self.countSubsequnce(arr,k))
        
        for i in ans:
            print(i, end=" ")
        print()




# time complexity: O(n^3)
# space complexity: O()
if __name__ == "__main__":  
    for _ in range(1):
        print(Solution().run())