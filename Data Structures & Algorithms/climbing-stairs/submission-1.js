class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        if (n <= 2) return n;

        let first = 1;
        let second = 2;

        for (let i = 3; i <= n; i++) {
            let curr = first + second;

            first = second;
            second = curr;
        }

        return second;
    }
}
