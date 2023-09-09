class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n <= 10:
            count = 0
            fac = 1
            for i in range(1, n+1):
                if fac%10 == 0:
                    count += 1
                    fac //= 10
                fac *= i
            if fac%10 == 0:
                count += 1
            return count
        else:
            count = 0
            for j in range(5, n+1, 5):
                temp = j
                while temp%5 == 0:
                    count += 1
                    temp //= 5
            return count