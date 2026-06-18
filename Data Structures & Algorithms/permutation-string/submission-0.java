class Solution {
    public boolean isPermutation(Map<Character, Integer> d1, Map<Character, Integer> d2){
        return d1.equals(d2);
    }
        

    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) { return false; }

        //check permutations by having the same # of letters in hashmap
        //first initialize d1 as the answerkey
        //initialize d2 with as much letters as s1

        Map<Character, Integer> d1 = new HashMap<>();
        Map<Character, Integer> d2 = new HashMap<>();

        for (char c: s1.toCharArray()){
            d1.put(c, d1.getOrDefault(c, 0) + 1);
        }

        for (char c: s2.substring(0, s1.length()).toCharArray()){
            d2.put(c, d2.getOrDefault(c, 0) + 1);
        }

        if (isPermutation(d1, d2)){
            return true;
        }
        int l = 0;
        for (int j = s1.length(); j < s2.length(); j++){
            char letter = s2.charAt(j);
            //add the new letter
            d2.put(letter, d2.getOrDefault(letter, 0)+1);

            //remove from left boundary
            char leftchar = s2.charAt(l);
            d2.put(leftchar, d2.get(leftchar)-1);
            if (d2.get(leftchar) == 0) {
                d2.remove(leftchar);
            }
            if (isPermutation(d1, d2)) {
                return true;
            }
            l++;
        }

        return isPermutation(d1, d2);
        
        
    }
}
