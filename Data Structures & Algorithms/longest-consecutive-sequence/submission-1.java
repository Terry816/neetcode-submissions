class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) { return 0; }
        Set<Integer> set = new HashSet<>();
        for (int n: nums) {
            set.add(n);
        }
        int longest = 1;

        for (int n : set){
            if (!set.contains(n-1)) {
                int i = 0;
                while (set.contains(n+i)){
                    i++;
                }
                longest = Math.max(i, longest);
            }
        }

        return longest;

    }
}