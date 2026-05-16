class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    countSubstrings(s) {
        const n = s.length;
        
        let dp = Array.from({ length: n }, () => Array(n).fill(false));
        let count = 0;

        for (let i = 0; i < n; i++) {
            dp[i][i] = true;
            count += 1;
        }

        for (let i = n - 1; i >= 0; i--) {
            for (let j = i + 1; j < n; j++) {
                if (s[i] == s[j]) {
                    if ((j - i == 1) || (dp[i + 1][j - 1])) {
                        dp[i][j] = true;
                        count += 1;
                    }
                }
            }
        }

        return count;
    }
}
