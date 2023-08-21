class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        last = len(s) - 1

        for first in range(len(s)):
            if last > first:
                s[first], s[last] = s[last], s[first]
                last -= 1