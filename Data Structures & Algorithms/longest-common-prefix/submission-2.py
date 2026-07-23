class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        ans = ""

        first = strs[0]
        last = strs[-1]

        for i in range (min(len(first), len(last))):
            if first[i] == last[i]:
                ans += first[i]
            else:
                break
        return ans

                    