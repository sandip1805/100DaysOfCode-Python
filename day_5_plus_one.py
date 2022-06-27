class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=''
        for i in digits:
            x += str(i)
        result = []
        for c in str(int(x) + 1):
            result.append(c)
        return result