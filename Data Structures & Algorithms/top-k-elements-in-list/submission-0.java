class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num: nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<List<Integer>> buckets = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++ ){
            buckets.add(new ArrayList<>());
        }

        for (Map.Entry<Integer, Integer> entry: map.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();

            buckets.get(freq).add(num);
        }
        
        int[] res = new int[k];
        int idx = 0;

        for (int i = buckets.size() -1; i > 0; i--){
            List<Integer> bucket = buckets.get(i);
            for (int num: bucket){
                res[idx] = num;
                idx++;
                if (idx == k){
                    return res;
                }
            }
        }
        return res;

    }
}