from typing import List,Optional
from collections import deque
import sys, math
class Solution:
    # def run(self):
    #     l,r = list(map(int,input().strip().split()))
        
    #     s = math.ceil(math.log(l,3))
    #     if(3**s==l):s+=1
    #     start = s
    #     power = 3**s
    #     ans = 0
    #     if(power>r):return (r-l+1)*s+start
    #     else:ans+=(power-l)*s
            
    #     while(power*3<=r):
    #         s+=1
    #         ans+=(3*power-power)*s
    #         power*=3
        
    #     s+=1
    #     ans+=(r-power+1)*s
    #     return ans+start
    
    def run(self):
        l,r = list(map(int,input().strip().split()))
        ans = p[r]+p[l]
        if(l>0):ans-=2*p[l-1]
        return ans
        
        
# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    size = 2*(10**5)+1
    arr = [0]*size
    for num in range(1,size):
        k = num
        cnt = 0
        while(k):
            cnt+=1
            k//=3
        arr[num] = cnt
    
    p = [0]*size
    for i in range(1,size):
        p[i] = p[i-1]+arr[i]
    
    for _ in range(int(input().strip())):
        print(Solution().run())