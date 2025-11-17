"""
Set Matrix Zero
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 
and then return the matrix.

Examples 1:

Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

Output: [[1,0,1],[0,0,0],[1,0,1]]

Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0
"""

def matrix(mat):

    row = len(mat)
    col = len(mat[0])

    for r in range(row):
        for c in range(col):
            if mat[r][c] == 0:
                for i in range(col):
                    mat[r][i] = '#'
                for j in range(row):
                    mat[j][c] = '#'


    for i in range(row):
        for j in range(col):
            if mat[i][j] == '#':
                mat[i][j] = 0
    return mat

# Example usage
mat = [[1,1,0],[1,0,1],[1,1,1]]
print(matrix(mat))  # Output: [[1,0,1],[0,0,0],[1,0,1]]