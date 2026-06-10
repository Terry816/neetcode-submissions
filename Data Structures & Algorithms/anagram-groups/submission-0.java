class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String word : strs) {
            char[] arr = word.toCharArray();
            Arrays.sort(arr);
            String sorted = new String(arr);
            if (map.containsKey(sorted)){
                map.get(sorted).add(word);
            } else {
                List<String> group = new ArrayList<>();
                group.add(word);
                map.put(sorted, group);
            }
        }
        return new ArrayList<>(map.values());
    }
}