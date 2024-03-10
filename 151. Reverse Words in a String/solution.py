class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        a= " ".join(s.split())
        b= a.split(" ")
        reverse = b[::-1]
        result = " ".join(reverse)
        return result