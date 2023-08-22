class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                temp = word[:(i+1)][::-1]
                word = temp + word[(i+1):]
                break
        return word