class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        alpha_num_str = ([char for char in s if char.isalnum()])
        alpha_num_str_reverse = ([char for char in s if char.isalnum()])
        alpha_num_str_reverse.reverse()

        return "".join(alpha_num_str) == "".join(alpha_num_str_reverse)