class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;

        int low = 0, high = m*n - 1;
        while(low<=high) {
            int mid = (low + high)/2;
            int actual = matrix[mid/n][mid%n];
            // System.out.println("low: "+low+" high: "+high+" mid: "+mid+" actual: "+actual);
            if (actual>target) {
                high = mid-1;
            } else if(actual<target) {
                low = mid+1;
            } else {
                return true;
            }
        }
        return false;
    }
}
