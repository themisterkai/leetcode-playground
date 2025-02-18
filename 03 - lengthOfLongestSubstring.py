class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_len = 0

        for i in range(len(s)):
            substring_index = i
            substring_end = i+1
            while len(s[substring_index:substring_end]) == len(set(s[substring_index:substring_end])) and \
                substring_end < len(s)+1:
                if len(s[substring_index:substring_end]) > longest_substring_len:
                    longest_substring_len = len(s[substring_index:substring_end])
                substring_end += 1
            if len(s[i:]) < longest_substring_len:
                break
            
   
        return longest_substring_len

        

s_input = "dvdf"
solution = Solution()
print(solution.lengthOfLongestSubstring(s_input))