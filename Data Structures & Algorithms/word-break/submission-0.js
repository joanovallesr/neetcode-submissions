class Solution {
    wordBreak(s, wordDict) {
        // Convert dictionary to a set for O(1) lookups
        const wordSet = new Set(wordDict);
        
        // Optimization: Find the length of the longest word in the dictionary
        const maxLen = wordSet.size > 0 ? Math.max(...Array.from(wordSet).map(w => w.length)) : 0;
        
        const n = s.length;
        // dp[i] will be True if s[0:i] can be segmented into valid words
        const dp = new Array(n + 1).fill(false);
        
        // Base case: An empty string is always considered validly segmented
        dp[0] = true;
        
        // Fill out the dp array
        for (let i = 1; i <= n; i++) {
            // Optimization: Only look back up to maxLen characters
            for (let j = Math.max(0, i - maxLen); j < i; j++) {
                // If s[0:j] is valid and s[j:i] is a valid word, then s[0:i] is valid
                if (dp[j] && wordSet.has(s.substring(j, i))) {
                    dp[i] = true;
                    break; // Found a valid split point for prefix i, move to next i
                }
            }
        }
        
        return dp[n];
    }
}