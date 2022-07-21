from typing import List
import math


def merge(nums1: List[int], nums2: List[int], nums: List[int]):
    i = 0
    j = 0
    k = len(nums1) + len(nums2)
    for idx in range(0, k):
        if i == len(nums1) and j < len(nums2):
            nums[idx] = nums2[j]
            j += 1
            continue
        if j == len(nums2) and i < len(nums1):
            nums[idx] = nums1[i]
            i += 1
            continue
        if nums1[i] <= nums2[j]:
            nums[idx] = nums1[i]
            i += 1
        else:
            nums[idx] = nums2[j]
            j += 1


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = len(nums1) + len(nums2)
        nums = [0] * k
        merge(nums1, nums2, nums)
        odd = len(nums) % 2
        if odd:
            center = math.floor(k / 2)
            return nums[center]
        else:
            center1 = math.floor(k / 2) - 1
            center2 = math.floor(k / 2)
            return (nums[center1] + nums[center2]) / 2


if __name__ == "__main__":
    print("We are back")
    nums1 = [1, 3]
    nums2 = [2, 4]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))
