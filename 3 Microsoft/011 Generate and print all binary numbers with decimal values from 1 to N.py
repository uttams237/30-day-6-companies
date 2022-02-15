#Function to generate binary numbers from 1 to N using a queue.
def generate(N):
    
    def tobin(n):
        ans=""
        while n>0:
            ans+= str(n%2)
            n=n//2
            
        return ans[::-1]
        
        
    ans=[]
    for i in range(1,n+1):
        ans.append(tobin(i))
        
    return ans
