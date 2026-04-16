class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int r = 0; // first row 
        int c = matrix[0].length - 1; // most right

        while ((r < matrix.length) && (c >= 0)) {
            int val = matrix[r][c];
            if (val == target) {
                return true;
            } else if (val < target) {
                r++;
            } else {
                c--;
            }
        }
        return false;
    }
}