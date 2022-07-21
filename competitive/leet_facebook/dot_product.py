from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def __iter__(self):
        return self.nums.__iter__()

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for idx, val in enumerate(vec):
            result += val * self.nums[idx]
        return result


# Your SparseVector object will be instantiated and called as such:
if __name__ == '__main__':
    nums1 = [1,0,0,2,3]
    nums2 = [0,3,0,4,0]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    ans = v1.dotProduct(v2)
    print(ans)