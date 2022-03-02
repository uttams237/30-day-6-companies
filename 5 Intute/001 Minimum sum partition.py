class Solution:
	def minDifference(self, arr, n):
        s= sum(arr)
        half= s//2
        if s%2:
            half+=1
        
        dp= [[0 for i in range(n+1)] for j in range(half+1)]
        
        for i in range(n+1):
            dp[0][i]=1
            
        for j in range(1,half+1):
            for i in range(1,n+1):
                if j==arr[i-1]:
                    dp[j][i]=1
                else:
                    temp=0
                    if j-arr[i-1] >=0:
                        temp=dp[j-arr[i-1]][i-1]
                    dp[j][i]= max(temp , dp[j][i-1])

        # for ele in dp :
        #   print(ele)
                    
        big=0
        for j in range(half,-1,-1):
            if dp[j][-1]==1:
                big= j
                break
            
        return abs(s-(2*big))
