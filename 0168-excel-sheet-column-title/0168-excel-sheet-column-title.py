class Solution(object):
    def convertToTitle(self, columnNumber):
        result = ''
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            char = chr(ord('A') + rem)
            result = char + result
            columnNumber = columnNumber // 26
        return result