class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_list = []
        for each in s:
            ascii_list.append(ord(each))
        l = 0
        r = 1
        sums = 0
        while(r<len(ascii_list)):
            sums+=abs(ascii_list[r]- ascii_list[l])
            l+=1
            r+=1
        return sums
        

        