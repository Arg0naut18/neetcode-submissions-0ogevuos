class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] l = new int[n];
        int[] r = new int[n];
        l[0] = height[0];
        r[n-1] = height[n-1];
        for(int i=1; i<n; i++) {
            l[i] = Math.max(l[i-1], height[i]);
            r[n-i-1] = Math.max(r[n-i], height[n-i-1]);
        }
        int sum = 0;
        for(int i=0; i<n; i++) {
            sum += Math.abs(height[i]-(Math.min(l[i], r[i])));
        }
        return sum;
    }
}
