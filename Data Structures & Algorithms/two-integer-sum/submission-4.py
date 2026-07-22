from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = nums.copy() 
        nums.sort()

        i, j = 0, len(nums) - 1
        val1, val2 = None, None

        while i < j:
            current_sum = nums[i] + nums[j]
            if current_sum == target:
                val1 = nums[i]
                val2 = nums[j]
                break
            elif current_sum > target:
                j -= 1
            else:
                i += 1
        
        first_idx = temp.index(val1)

        if val1 == val2:
            sec_idx = temp.index(val2, first_idx + 1)
        else:
            sec_idx = temp.index(val2)

        return sorted([first_idx, sec_idx])
