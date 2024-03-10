class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        temp = []
        for i in range(len(s)):
            if s[i] in vowels:
                temp.append(s[i])
        temp_new = temp[::-1]
        j=0
        temp2= []
        for i in range(len(s)):
            if s[i] in vowels:
                temp2.append(temp_new[j]) 
                j+=1
            else:
                temp2.append(s[i]) 
        result = ''.join(str(x) for x in temp2)
        return result