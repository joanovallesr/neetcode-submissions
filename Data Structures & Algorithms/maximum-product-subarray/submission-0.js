class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxProduct(nums) {
        let globalMax = nums[0];
        let currMax = nums[0];
        let currMin = nums[0];

        for (let i = 1; i < nums.length; i++) {
            const num = nums[i];

            const tempMax = Math.max(num, currMax * num, currMin * num);
            currMin = Math.min(num, currMax * num, currMin * num);

            currMax = tempMax;
            globalMax = Math.max(globalMax, currMax);
        }

        return globalMax;
    }
}
