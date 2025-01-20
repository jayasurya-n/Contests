from typing import List
from math import gcd
import sys
class Solution:
    def gcd(self,a, b):
        while b:
            a,b = b,a%b
        return a

    def MaxDiff(self, n : int, arr : List[int]) -> int:
        maxIndex = [-1]*1001
        minIndex = [n+1]*1001

        for i in range(n):
            maxIndex[arr[i]] = max(i,maxIndex[arr[i]])
            minIndex[arr[i]] = min(i,minIndex[arr[i]])

        ans = -1
        for i in range(1,1001):
            for j in range(1,1001):
                if(maxIndex[i]==-1 or maxIndex[j]==-1):continue
                elif(gcd(i,j)!=1):continue
                ans = max(ans,abs(maxIndex[i]-minIndex[j]))
                ans = max(ans,abs(maxIndex[j]-minIndex[i]))
        return ans


# time complexity: O(n)*O(log(1000)) 
# space complexity: O(1001)==O(1)
t = int(input().strip())                
if __name__ == "__main__":
    for i in range(t):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().MaxDiff(n,arr))
