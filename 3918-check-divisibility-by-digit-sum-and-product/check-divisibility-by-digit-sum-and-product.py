class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dSum = 0
        dProd = 1
        for i in str(n):
            temp = int(i)
            dSum += temp
            dProd *= temp
        return n % (dSum + dProd) == 0