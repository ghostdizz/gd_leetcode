class Solution:
    def romanToInt(self, s: str) -> int:
        string_list = list(s)
        dictionary = {"I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(string_list)):
            char_replace = string_list[i]
            string_list[i] = dictionary[char_replace]
        sum_list = 0
        for j in range(len(string_list) - 1):
            if string_list[j] < string_list[j + 1]:
                sum_list -= string_list[j]
            else:
                sum_list += string_list[j]
        sum_list += string_list[-1]
        return sum_list