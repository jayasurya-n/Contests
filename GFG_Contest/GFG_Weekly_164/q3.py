from typing import List,Optional
import sys
class Solution:
    def countSubarrays(self, n : int, arr : List[int]) -> int:
        ans = 0
        for i in range(n):
            mini = 27
            maxi = -1
            for j in range(i,min(n,i+52)):
                mini = min(mini,arr[j])
                maxi = max(maxi,arr[j])
                if((mini+maxi)%(j-i+1)==0):ans+=1
        return ans
    



# time complexity: O(52*n)
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().countSubarrays(n,arr))