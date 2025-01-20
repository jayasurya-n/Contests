class Solution:
    def splitPermutation(self,n):
        if(n==1):return [1]
        if(n==2):return [1,2]

        if(n%2==0):i,j=1,n
        if(n%2==1):i,j=1,n-1
        
        ans = []
        while(i<j):
            ans.append(i)
            ans.append(j)
            i+=1
            j-=1
        if(n%2==1):ans.append(n)
        return ans

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    ans = Solution().splitPermutation(n)
    for i in ans:
        print(i,end = " ")
    print()
