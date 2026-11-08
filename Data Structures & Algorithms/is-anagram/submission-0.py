class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1=dict(Counter(s))
        dict_2=dict(Counter(t))
        if dict_1==dict_2:
            return True
        return False