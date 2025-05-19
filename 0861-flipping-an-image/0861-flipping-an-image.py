class Solution:
    def flipAndInvertImage(self, image):
        flipped = [row[::-1] for row in image]
        inverted = [[1 - pixel for pixel in row] for row in flipped]
        return inverted
        