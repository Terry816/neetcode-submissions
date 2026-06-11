class Solution {
    public void reverseString(char[] s) {
        int len = s.length / 2;
        int j = s.length - 1;
        for (int i = 0; i < len; i++){
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            j--;
        }
    }
}