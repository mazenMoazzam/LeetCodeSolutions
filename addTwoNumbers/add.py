class Solution(object):
    def getSum(self, a, b):
        MASK = 0xFFFFFFFF     
        MAX_INT = 0x7FFFFFFF  
        while b != 0:
            sumWithoutCarry = (a ^ b) & MASK
            carrySum = ((a & b) << 1) & MASK
            
            a = sumWithoutCarry
            b = carrySum
        
        if a <= MAX_INT:
            return a
        else:
            return ~(a ^ MASK)
