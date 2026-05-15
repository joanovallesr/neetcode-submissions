class Solution {
    /**
     * @param {string} text1
     * @param {string} text2
     * @return {number}
     */
    longestCommonSubsequence(text1, text2) {
        const m = text1.length;
        const n = text2.length;

        let curr = new Array(n + 1).fill(0);
        let prev = new Array(n + 1).fill(0);

        for (let i = 1; i <= m; i++) {
            for (let j = 1; j <= n; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    curr[j] = 1 + prev[j - 1];
                } else if (j > 0) {
                    curr[j] = Math.max(curr[j - 1], prev[j]);
                }
            }

            prev = curr;
            curr = new Array(n + 1).fill(0);
        }
        return prev[n];
    }
}
