class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        final=[]
        for each in s:
            if each.isalnum():
                final.append(each)
        final_reverse= final.copy()
        final.reverse()
        return final == final_reverse
        