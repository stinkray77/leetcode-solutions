class Solution {
    public int searchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.length;

        while (low < high) {
            int mid = low + (high - low) / 2;
            int val = nums[mid];
        
            if (val < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return high;
    }
}