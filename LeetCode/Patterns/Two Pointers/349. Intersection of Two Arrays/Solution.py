class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        if len(s1)<len(s2):
            s1,s2 = s2,s1
        a = []
        for x in s1:
            if x in s2:
                a.append(x)
        return a