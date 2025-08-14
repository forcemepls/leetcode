class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        s_list = list(s)
        s_set = {}
        total, total_max = 1, -1
        for i in range(len(s_list) - 1):
            



def main():
    solution = Solution()
    s = input()
    print(solution.length_of_longest_substring(s))

if __name__ == '__main__':
    main()