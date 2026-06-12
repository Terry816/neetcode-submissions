class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        /*
        Pointer on ends of both arrays.
        Compare and store the greater value.
        if nums1 empties first -> fill in rest of values till nums2 runs out
        if nums2 empties first -> dont do anything just return
        [1, 2, 3, 0, 0, 0]
        [2, 5, 6]
        */
        if (n==0) { return; }

        int i = m-1, j = n-1;
        int p = n + m - 1;
        while (i >= 0 && j >= 0){
            int n1 = nums1[i], n2 = nums2[j];
            System.out.printf("%d, %d\n", n1, n2);
            if (n2 >= n1){
                nums1[p] = n2;
                j--;
            } else {
                nums1[p] = n1;
                i--;
            }
            p--;
        }
        while (j >= 0){
            nums1[p] = nums2[j];
            j--;
            p--;
        }
        
    }
}