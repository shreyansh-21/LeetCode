class Solution {
    public int[] constructTransformedArray(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            int newIndex = ((i + nums[i]) % n + n) % n;
            ans[i] = nums[newIndex];
        }

        return ans;
    }
}
