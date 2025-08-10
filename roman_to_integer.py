symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

class Solution:
    @staticmethod
    def list_collection(s_list: list) -> list:
        indexes = list()
        for i in range(len(s_list) - 1):
            t = s_list[i] + s_list[i + 1]
            if t in {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}:
                indexes.append(i)
        return indexes

    @staticmethod
    def counting(s_list: list, indexes: list) -> int:
        i = 0
        total = 0
        while i < len(s_list):
            if i in indexes:
                total += symbols[s_list[i + 1]] - symbols[s_list[i]]
                i += 2
            else:
                total += symbols[s_list[i]]
                i += 1
        return total

    def roman_to_int(self, s: str) -> int:
        s_list = list(s)
        indexes = self.list_collection(s_list)
        result = self.counting(s_list, indexes)
        return result


def main():
    s = input('Введите римское число: ')
    solution = Solution()
    result = solution.roman_to_int(s)
    print(result)

if __name__ == '__main__':
    main()