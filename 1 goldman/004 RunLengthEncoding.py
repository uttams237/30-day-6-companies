def encode(s):
    ans=""
    letter,count=s[0],0
    
    i=0
    while i<len(s):
        if s[i]==letter:
            count+=1
        else:
            ans+=letter
            ans+= str(count)
            letter=s[i]
            count=1
            
        i+=1
        
    ans+=letter
    ans+= str(count)
    
            
    return ans
