class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    longestPalindrome(s) {
        if (!s || s.length < 1) return "";

        let start = 0;
        let end = 0;

        function expandFromCenter(left, right) {

            while (left >= 0 && right < s.length && s[left] == s[right]) {
                left -= 1;
                right += 1;
            }

            return right - left - 1;
        }

        for (let i = 0; i < s.length; i++) {

            const len1 = expandFromCenter(i, i);
            const len2 = expandFromCenter(i, i + 1)
            const maxLen = Math.max(len1, len2)

            if (maxLen > (end - start)) {
                start = i - Math.floor((maxLen - 1) / 2);
                end = i + Math.floor(maxLen / 2);
            }
        }

        return s.slice(start, end + 1);
    }
}
