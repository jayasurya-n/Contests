from typing import List
import sys
class Solution:
    def MinSize(self, n : int, arr : List[int]) -> int:
        freq = {}
        for i in range(n):
            freq[arr[i]] = freq.setdefault(arr[i],0)+1
        
        maxFreq = -1
        for key,value in freq.items():
            maxFreq = max(maxFreq,value)
        
        if(maxFreq>=n/2):
            return maxFreq-(n-maxFreq)
        elif(n%2==1):return 1
        else:return 0
        
# time complexity: O(n) 
# space complexity: O(n)            
t = int(input().strip())
if __name__ == "__main__":
    for t in range(t):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().MinSize(n,arr))