class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans = []
        l = len(nums)

        for i in range (l-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    break
        
        return ans