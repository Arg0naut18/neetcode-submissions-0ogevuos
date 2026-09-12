class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> tempsMono = new Stack<Integer>();
        int[] result = new int[temperatures.length];
        for(int i=0; i<temperatures.length; i++) {
            while (!tempsMono.isEmpty() && temperatures[tempsMono.peek()]<temperatures[i]) {
                int zeroIdx = tempsMono.pop();
                result[zeroIdx] = i - zeroIdx;
            }
            tempsMono.push(i);
        }
        return result;
    }
}
