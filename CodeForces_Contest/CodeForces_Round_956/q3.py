from typing import List,Optional
import sys
class Solution:
    def solve(self,a,b,c):
        target = (sum(a)+3-1)//3
        
        i = 0
        ans = []
        aSum,bSum,cSum = 0,0,0
        while(i<len(a)):
            aSum+=a[i]
            bSum+=b[i]
            cSum+=c[i]

            if(len(ans)==0 and aSum>=target):
                ans.append(i+1)
                aSum,bSum,cSum = 0,0,0
                
            elif(len(ans)==1 and bSum>=target):
                ans.append(i+1)
                aSum,bSum,cSum = 0,0,0

            elif(len(ans)==2 and cSum>=target):
                ans.append(i+1)
                aSum,bSum,cSum = 0,0,0

            i+=1
        return ans


    def run(self):
        n = int(input().strip())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        c = list(map(int,input().strip().split()))

            
        ans = self.solve(a,b,c) 
        if(len(ans)==3):
            return [1,ans[0],ans[0]+1,ans[1],ans[1]+1,n]
        
        ans = self.solve(a,c,b)
        if(len(ans)==3):
            return [1,ans[0],ans[1]+1,n,ans[0]+1,ans[1]]

        ans = self.solve(b,a,c)
        if(len(ans)==3):  
            return [ans[0]+1,ans[1],1,ans[0],ans[1]+1,n]

        ans = self.solve(b,c,a)
        if(len(ans)==3):
            return [ans[1]+1,n,1,ans[0],ans[0]+1,ans[1]]

        ans = self.solve(c,a,b)
        if(len(ans)==3):
            return [ans[0]+1,ans[1],ans[1]+1,n,1,ans[0]]

        ans = self.solve(c,b,a)
        if(len(ans)==3):    
            return [ans[1]+1,n,ans[0]+1,ans[1],1,ans[0]]
    
        return [-1]



# time complexity: O(6*n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = Solution().run()
        for i in arr:
            print(i,end= " ")
        print()