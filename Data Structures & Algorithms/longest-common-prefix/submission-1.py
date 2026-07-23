class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_string = min(strs, key=len)

        ans = ""

        for i in range (1, len(smallest_string)+1):
            subString = smallest_string[0:i]
            flag = True

            for word in strs:
                if word.startswith(subString) == False:
                    flag = False
                    break
            
            if flag:
                ans = subString

        return ans
                    