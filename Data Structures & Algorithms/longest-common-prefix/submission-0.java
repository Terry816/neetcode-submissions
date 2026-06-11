class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0){ return ""; }

        //find the smallest length string in the array and iterate through that length
        //check the rest of the strings if they have a matching char

        int smallestLength = 201;
        String smallestWord = strs[0];
        for (String word: strs){
            if (word.length() < smallestLength){
                smallestLength = word.length();
                smallestWord = word;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < smallestLength; i++){
            char letter = smallestWord.charAt(i);
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