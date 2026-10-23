class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        f = 0
        if len(s1)>len(s2):
            f = 1
        else:
            f = 0
        l = []
        if f:
            for i in s1:
                if i in s2:
                    l.append(i)
        else:
            for i in s2:
                if i in s1:
                    l.append(i)
        return l

        