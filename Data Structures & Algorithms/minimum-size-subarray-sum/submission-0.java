class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        if (nums.length == 0) { return 0; }
        int smallest = nums.length + 1;
        int l =0;
        int curSum = 0;
        for (int r = 0; r < nums.length; r++){
            curSum += nums[r];
            while (curSum >= target) {
                smallest = Math.min(smallest, (r-l+1));
                curSum -= nums[l];
                l++;
            }
        }

        return smallest == nums.length +1 ? 0: smallest;
    }
}