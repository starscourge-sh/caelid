class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = [ord(char) for char in s]
        t_arr = [ord(char) for char in t]
        s_arr.sort()
        t_arr.sort()
        return s_arr == t_arr