class Solution:
    def makePermutation(self,arr,n):
        arr.sort()
        while(n>0):
            if(arr[n-1]>n):return "NO"
            n-=1
            arr.pop()
        return "YES"


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    arr = list(map(int,input().strip().split()))
    print(Solution().makePermutation(arr,n))
