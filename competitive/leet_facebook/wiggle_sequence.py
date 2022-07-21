from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        wiggle_nums = []

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        # len 2 onwards
        first = nums[0]
        second = nums[1]
        flag = "first"
        wiggle_nums.append(first)
        last = first
        if second < first:
            flag = "next_large"
            wiggle_nums.append(second)
            last = second
        elif second > first:
            flag = "next_small"
            wiggle_nums.append(second)
            last = second
        else:
            flag = "first"

        indx = 2
        while indx < len(nums):
            if flag == "next_large" and last < nums[indx]:
                last = nums[indx]
                wiggle_nums.append(nums[indx])
                flag = "next_small"
            elif flag == "next_small" and last > nums[indx]:
                last = nums[indx]
                wiggle_nums.append(nums[indx])
                flag = "next_large"
            elif flag == "first":
                second = nums[indx]
                if second < first:
                    flag = "next_large"
                    wiggle_nums.append(second)
                elif second > first:
                    flag = "next_small"
                    wiggle_nums.append(second)
                else:
                    flag = "first"
                last = second
            else:
                print("Skip")
            indx += 1

        return len(wiggle_nums)

# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         print("+++++++++++++++++++")
#         print(nums)
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return 1
#         diff_array = list()
#         sign_array = list()
#         diff_array.append(-1)
#         x = 0
#         while x < len(nums)-1:
#             diff_array.append(nums[x+1]-nums[x])
#             x += 1
#         print(diff_array)
#
#         y = 0
#         past = diff_array[0]
#         while y < len(diff_array):
#             if y == 0:
#                 sign_array.append(-1)
#                 y += 1
#                 continue
#             present = diff_array[y]
#             signvalue = past * present
#             if past == 0 and present != 0:
#                 sign_array.append(-1)
#             elif signvalue < 0:
#                 sign_array.append(-1)
#             else:
#                 sign_array.append(1)
#
#             past = diff_array[y]
#             y += 1
#         print(sign_array)
#         count_max = 0
#         for z in sign_array:
#             if z == -1:
#                 count_max += 1
#
#         # max = 0
#         # cur_max = 0
#         # point_max = 0
#         # start_point_cur_max = 0
#         # for idx, val in enumerate(sign_array):
#         #     print(idx,val)
#         #     if val == -1:
#         #         cur_max += 1
#         #     else:   # reset
#         #         if cur_max > max:
#         #             max = cur_max
#         #             point_max = start_point_cur_max
#         #
#         #         cur_max = 0
#         #         start_point_cur_max = idx
#         # if cur_max > max:
#         #     max = cur_max
#         #     point_max = start_point_cur_max
#         print("++++++++++++++++++++")
#         return count_max


mysol = Solution()


if __name__ == "__main__" :
    # print(mysol.wiggleMaxLength([1, 7, 4, 9, 2, 5]))
    # print(mysol.wiggleMaxLength([1, 4, 7, 2, 5]))
    print(mysol.wiggleMaxLength([1, 7, 4, 5, 5]))
    # print(mysol.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
    # print(mysol.wiggleMaxLength([0, 0]))
    # print(mysol.wiggleMaxLength([3, 3, 3, 2, 5]))
