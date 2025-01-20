from typing import List,Optional
import sys
class Solution:
    def count(self,s):
        zero,one = 0,0
        for i in range(len(s)):
            if(s[i]=='0'):zero+=1
            else:one+=1
        return zero,one

    def run(self) -> Optional[list]:
        n,k = list(map(int,input().strip().split()))
        s = input().strip()
        t = input().strip()

        # print(self.count(s),self.count(t))
        if(self.count(s)!=self.count(t)):return "NO"
        if(s=="00" or s=="11"):return "YES"
        if(s=="01" or s=="10"):
            if(s==t):
                if(k%2==0):return "YES"
                else:return "NO"
            else:
                if(k%2==1):return "YES"
                else:return "NO"

        
        if(s==t):return "YES"
        cnt=0
        for i in range(len(s)):
            if(s[i]!=t[i]):cnt+=1
        
        if(cnt<=2*k):return "YES"
        return "NO"


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())