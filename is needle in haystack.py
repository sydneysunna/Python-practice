class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # read haystack and read needle, see if needle = 0 of hastack
        if needle in haystack:
           return haystack.index(needle)
        else:
            return -1