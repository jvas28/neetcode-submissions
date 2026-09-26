class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        d1 = self.toDict(s)
        d2 = self.toDict(t)
        return d1 == d2
    
    def toDict(self, s:str) -> dict:
        res = {}
        for char in s:
            if char not in res:
                res[char]=0
            else:
                res[char] += 1
        return res;