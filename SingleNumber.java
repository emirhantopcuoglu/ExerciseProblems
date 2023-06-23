import java.util.Arrays;
// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
// You must implement a solution with a linear runtime complexity and use only constant extra space.
public class SingleNumber {
    public static int singleNumber(int[] nums) {
        int i;
        if (nums.length == 1) {
            return nums[0];
        }
        Arrays.sort(nums);
        for (i = 0; i < nums.length - 1; i += 2) {
            if (nums[i] != nums[i + 1]) {
                return nums[i];
            }
        }
        return nums[nums.length - 1];
    }

    public static void main(String args[]) {
        /*
         * Example:
         * int[] nums = {2,2,1};
         * System.out.println(SingleNumber.singleNumber(nums));
         */
    }
}