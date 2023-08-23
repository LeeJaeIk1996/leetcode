class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest_pal = ""

        for first in range(len(s)):
            tmp = ""
            for second in range(first, len(s)):
                st = s[second]
                tmp += st
                if tmp == tmp[::-1] and len(tmp) > len(longest_pal):
                    longest_pal = tmp

        return longest_pal