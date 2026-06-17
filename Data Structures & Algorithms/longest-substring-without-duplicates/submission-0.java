class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int l = 0, res = 0;
        for (int r = 0; r < s.length(); r++){
            char letter = s.charAt(r);
            while (seen.contains(letter)){
                seen.remove(s.charAt(l));
                l++;
            }
            seen.add(letter);
            res = Math.max(res, (r-l+1));
        }
        return res;
    }
}
