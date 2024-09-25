class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        currentIndex = 0
        for letter in t:
            if letter == s[currentIndex]:
                currentIndex += 1
            if len(s) == currentIndex:
                return True
        return False


sInput = "axc"
tInput = "ahbgdc"
solution = Solution()
print(solution.isSubsequence(sInput, tInput))