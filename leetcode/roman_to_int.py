from collections import OrderedDict

roman_to_int = OrderedDict([
    ('IV', 4), ('IX', 9), ('XL', 40), ('XC', 90),
    ('CD', 400), ('CM', 900),
    ('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100),
    ('D', 500), ('M', 1000)

])


class Solution:
    def romanToInt(self, s: str) -> int:
        ls = list(s)
        total = 0
        for k, v in roman_to_int.items():
            for i in range(len(ls) + 1 - len(k)):
                if len(k) == 1 and ls[i] == k[0]:
                    ls[i] = None
                    total += v
                elif len(k) == 2 and ls[i] == k[0] and ls[i + 1] == k[1]:
                    ls[i] = None
                    ls[i + 1] = None
                    total += v
        # print([i for i in roman_to_int.items()])
        return total


if __name__ == '__main__':
    ss = "MCMXCIV"
    s = Solution()
    print(s.romanToInt(ss))
