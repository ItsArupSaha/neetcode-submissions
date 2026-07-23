from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        # 1. Find the smallest string to set our maximum boundary
        smallest_string = min(strs, key=len)
        
        # 2. Use a pointer 'i' to track the character position
        for i in range(len(smallest_string)):
            current_char = smallest_string[i]
            
            # 3. Check if this exact character matches at index 'i' in all other words
            for word in strs:
                if word[i] != current_char:
                    # Mismatch found! Slice the prefix up to this index and return immediately
                    return smallest_string[:i]
                    
        # 4. If the loops finish, the entire smallest string is the prefix
        return smallest_string
