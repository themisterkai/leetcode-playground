class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

       
s_input = "   a good   example   "
solution = Solution()
print(solution.reverseWords(s_input))