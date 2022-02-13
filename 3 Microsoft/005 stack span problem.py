class Solution:
    def calculateSpan(self,a,n):
        ans=[1]
        stack=[0]
        
        for i in range(1,n):
            while len(stack)>0 and a[stack[-1]]<=a[i]:
                stack.pop()
                
            if len(stack)>0:
                ans.append(i-stack[-1])
            else:
                ans.append(i+1)
                
            stack.append(i)
                
        return ans
