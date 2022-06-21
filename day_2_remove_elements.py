class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i in range(0, len(nums)):
            if(val == nums[i]):
                continue
            nums[counter] = nums[i]
            counter += 1
        return counter