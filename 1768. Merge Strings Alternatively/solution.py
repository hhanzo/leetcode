class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        loop =0
        len_word1 = len(word1)
        len_word2 = len(word2)
        if len_word1 > len_word2:
            loop = len_word2
        else:
            loop = len_word1
        for i in range(loop):
            result = result + word1[i] + word2[i]
        #print(i)
        if len_word1 != len_word2:
            if len_word1 > len_word2:
                result = result + word1[i+1:len_word1]
            else: 
                result = result + word2[i+1:len_word2]        
        return result