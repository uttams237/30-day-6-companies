class Solution:
    def CountWays(self, s):
        n=len(s)
        
        dp=[0 for i in range(n)]
        
        if s[-1]!= "0":
            dp[-1]=1
            
        if n==1:
            return dp[0]
            
        if s[-2]!= "0":
            dp[-2]=dp[-1]
            
            if s[-2]=="1" or (s[-2]=="2" and (s[-1]!="7" and s[-1]!="8" and s[-1]!="9")):
           # if int(s[-2]+s[-1])<=26:
                dp[-2]+=1
                
        if n==2:
            return dp[0]
            
            
                
        for i in range(n-3,-1,-1):
            if s[i]!="0":
                dp[i]=dp[i+1]
               # if int(s[i]+s[i+1])<=26:
                if s[i]=="1" or (s[i]=="2" and (s[i+1]!="7" and s[i+1]!="8" and s[i+1]!="9")):
                    dp[i]+=dp[i+2]
                    
       # print(dp)
                    
        return dp[0]%(7+ (10**9))
