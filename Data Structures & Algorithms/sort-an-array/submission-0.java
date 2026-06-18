/*
nums = [3, 2, 4, 6, 5]
[3, 2, 4, 6, 5]
       p

[10,9,1,1,1,2,3,1]
> than pivot, skip over
less than pivot, swap with pivot spot
*/

class Solution {

    public void quickSort(int l, int r, int[] nums){
        if (l >= r){
            return;
        }
        int pivot = nums[r];
        int p = l;
        for (int i = l; i < r; i++){
            if (nums[i] < pivot){
                int temp = nums[p];
                nums[p] = nums[i];
                nums[i] = temp;
                p++;
            }
        }
        int temp = nums[p];
        nums[p] = pivot;
        nums[r] = temp;
        quickSort(l, p-1, nums);
        quickSort(p+1, r, nums);
    }

    public int[] sortArray(int[] nums) {
        //quicksort
        //pick a pivot, swap all numbers with that pivot
        // if they are strictly less than

        quickSort(0, nums.length-1, nums);
        return nums;
    }
}