class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(filter(str.isalnum, s)).lower()

        s_rev = s1[::-1]

        return s_rev == s1