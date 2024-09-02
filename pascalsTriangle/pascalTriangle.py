class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return [[]]

        pasTriangle = [[1]]

        for x in range(1, numRows):
            row =[1]
            previousRow = pasTriangle[-1]

            for j in range(1, x): 
                row.append(previousRow[j-1] + previousRow[j])
            
            row.append(1)

            pasTriangle.append(row)
        return pasTriangle
        
