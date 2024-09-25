import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()

        add = 0
        if len(s) % 2 != 0:
            add = 1

        s1 = s[0:math.ceil(len(s)/2)]
        s2 = s[math.ceil(len(s)/2)-add:len(s)]

        return s1 == s2[::-1]


sInput = "aba"
solution = Solution()
print(solution.isPalindrome(sInput))