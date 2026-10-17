
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = ""
        output = 0

        while r < len(s):
            if s[r] not in res:
                res += s[r]
                output = max(output, len(res))
                r += 1
            else:
                res = res[1:]
                l += 1

        return output
