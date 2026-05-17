class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        if (!nums) return 0;
        if (nums.length == 1) return nums[0];

        function robLinear(nums) {
            let rob1 = 0;
            let rob2 = 0;

            for (const num of nums) {
                let temp = Math.max(num + rob1, rob2);
                rob1 = rob2;
                rob2 = temp;
            }

            return rob2;
        }

        return Math.max(robLinear(nums.slice(1)), robLinear(nums.slice(0, -1)));
    }
}
