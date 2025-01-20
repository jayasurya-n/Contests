from typing import List
import sys
class Solution:
    def ANDequalOR(self, n : int, arr : List[int]) -> int:
        ans = 0;i=0
        while(i<n):
            j=i
            while j+1<n and arr[j]==arr[j+1]:
                j+=1
            ans+=((j-i+1)*(j-i+2))//2
            i = j+1
        return ans
            

# time complexity: O(n) 
# space complexity: O(1)
t = int(input().strip())  
if __name__ == "__main__":
    for i in range(t):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().ANDequalOR(n,arr))