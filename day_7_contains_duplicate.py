class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i in nums:
            if (duplicate.get(i)):
                return True
            else:
                duplicate[i] = True
        return False
            