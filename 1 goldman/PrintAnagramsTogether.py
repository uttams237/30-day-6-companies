class Solution:
    def Anagrams(self, words, n):
        
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        dict={}
        for ele in words:
            tempEle= str(sorted(ele))
            # print(tempEle)
            # print(type(tempEle))
            if tempEle in dict:
                dict[(tempEle)].append(ele)
            else:
                dict[(tempEle)]=[ele]
                
        ansArr=[]
        for key in dict:
            ansArr.append(dict[key])
            
        return ansArr
