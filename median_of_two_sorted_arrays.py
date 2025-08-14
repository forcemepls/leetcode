class Solution:
    @staticmethod
    def find_median_sorted_arrays(nums1: list, nums2: list) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        if len(nums) % 2 == 1:
            return float(nums[len(nums) // 2])
        else:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2


def main():
    solution = Solution()
    print(solution.find_median_sorted_arrays([1], [2,3]))
    print(solution.find_median_sorted_arrays([1, 2], [2, 3]))

if __name__ == '__main__':
    main()