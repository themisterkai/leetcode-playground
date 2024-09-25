class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        input_len = len(s)
        last_word_len = 0

        while input_len > 0:
            if s[input_len -1].isalpha():
                last_word_len += 1
                input_len -=1
            else:
                break
        return last_word_len

        

s_input = "   fly me   to   the moon  "
solution = Solution()
print(solution.lengthOfLastWord(s_input))