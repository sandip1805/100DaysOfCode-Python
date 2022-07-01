class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            nums2,nums1 = nums1, nums2    
        
        hashmap = {}
        for i in nums2:
            if i in hashmap:
                hashmap[i] = hashmap[i]+1
            else:
                hashmap[i] =1
        result = []

        #o(m)
        for i in nums1:
            if i in nums2 and hashmap[i] >0 :
                result.append(i)
                hashmap[i] = hashmap[i]-1
        return result