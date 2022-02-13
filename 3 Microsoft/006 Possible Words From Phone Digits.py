class Solution:
    def possibleWords(self,a,N):
        d={
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"]  ,
            5:["j","k","l"]  ,
            6:["m","n","o"]  ,
            7:["p","q","r","s"]  ,
            8:["t","u","v"] ,
            9:["w","x","y","z"] 
        }
        
        def help(a,n,i):
            if i==n-1:
                return d[a[i]]
                
            temp=help(a,n,i+1)
            ans=[]
            for ele in d[a[i]]:
                for word in temp:
                    ans.append(ele+word)
                    
            return ans
            
        ans= help(a,N,0)
        return ans
