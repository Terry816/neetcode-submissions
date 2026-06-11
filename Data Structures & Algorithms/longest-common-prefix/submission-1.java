class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0){ return ""; }

        //find the smallest length string in the array and iterate through that length
        //check the rest of the strings if they have a matching char

        int smallestLength = strs[0].length();
        for (String word: strs){
            smallestLength = Math.min(smallestLength, word.length());
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < smallestLength; i++){
            char letter = strs[0].charAt(i);
            for (String word: strs){
                if (letter != word.charAt(i)){
                    return sb.toString();
                }
            }
            sb.append(letter);
        }
        return sb.toString();
    }   
}