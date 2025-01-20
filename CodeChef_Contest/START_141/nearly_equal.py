from typing import List
import sys
class Solution:
    def hammingDistance(self,a,b):
        i=0
        ans = sys.maxsize
        while(i+len(b)<=len(a)):
            cnt=0
            for k in range(0,len(b)):
                if(a[k+i]!=b[k]):cnt+=1
            ans = min(ans,cnt)
            i+=1
        return ans

            
# time complexity: 
# space complexity: 
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n,m = list(map(int,input().strip().split()))
        a = input().strip()
        b = input().strip()
        print(Solution().hammingDistance(a,b))