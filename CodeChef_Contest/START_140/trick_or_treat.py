class Solution:
    def trickTreat(self,m,n,a,b):
        # cnt = 0
        # for i in range(n):
        #     for j in range(n):
        #         if((a[i]+b[j])%m==0):cnt+=1
        # return cnt
        cnt = 0
        rem_a = {}
        rem_b = {}

        for i in range(n):
            rem1 = a[i]%m
            rem2 = b[i]%m
            rem_a[rem1]  = rem_a.setdefault(rem1,0)+1
            rem_b[rem2]  = rem_b.setdefault(rem2,0)+1
        
        # print(rem_a,rem_b)
        for rem1 in rem_a.keys():
            cnt_a = rem_a[rem1]
            rem2 = (m-rem1)%m
            if(rem2 in rem_b):
                cnt_b = rem_b[rem2]
                cnt+= cnt_a*cnt_b
        return cnt

t = int(input().strip())
for i in range(t):
    n,m = list(map(int,input().strip().split()))
    a = list(map(int,input().strip().split()))
    b = list(map(int,input().strip().split()))
    print(Solution().trickTreat(m,n,a,b))
