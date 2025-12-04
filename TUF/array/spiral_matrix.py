"""
Docstring for TUF.array.spiral_matrix
Input: Matrix[][] = [[ 1, 2, 3, 4 ],[ 5, 6, 7, 8 ],[ 9, 10, 11, 12 ],[13, 14, 15, 16 ]]
Output: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.
Explanation: The output of matrix in spiral form.

Input: Matrix[][] = { { 1, 2, 3 }, { 4, 5, 6 },{ 7, 8, 9 } }
Output: 1, 2, 3, 6, 9, 8, 7, 4, 5.
Explanation: The output of matrix in spiral form.
"""

def spiral_matrix(matrix):

    result = []
    
    if not matrix:
        return result
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    direction = 0

    while top <= bottom and left <= right:
        if direction ==0:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
        
        elif direction == 1:
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

        elif direction == 2:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        else:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        direction = (direction + 1) % 4
    return result
# Example usage
matrix1 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
print(spiral_matrix(matrix1))  # Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

