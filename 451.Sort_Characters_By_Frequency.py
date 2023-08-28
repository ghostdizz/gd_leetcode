from collections import Counter, OrderedDict
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_by_value = sorted(count.items(), key=lambda x: x[1], reverse=True)
        string = ""
        for i in sorted_by_value:
            string += i[0] * i[1]
        return string

