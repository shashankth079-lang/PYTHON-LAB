class Solution:
    def spirallyTraverse(self, mat):
        result = []
        
        if not mat:
            return result
        
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1
        
        while top <= bottom and left <= right:
            
            # Traverse from left to right
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
            
            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            
            # Traverse from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1
            
            # Traverse from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
        
        return result
