class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(len(str1) < len(str2)):
            return self.gcdOfStrings(str2, str1)
     
        # If str1 is not the
        # concatenation of str2
        elif(not str1.startswith(str2)):
            return ""
        elif(len(str2) == 0):
         
        # GCD string is found
            return str1
        else:
         
        # Cut off the common prefix
        # part of str1 & then recur
            return self.gcdOfStrings(str1[len(str2):], str2)
 