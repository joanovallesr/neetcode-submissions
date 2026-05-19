class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    numDecodings(s) {
        // handle empty and leading zero edge cases
        if (!s || s[0] == "0") {
            return 0;
        }

        // track the last 2 numbers of decodes
        let downOne = 1;
        let downTwo = 1;

        for (let i = 1; i < s.length; i++) {
            let curr = 0;

            // check if single digit is valid
            if (s[i] != "0") {
                curr += downOne;
            }

            // check if double-digit is valid
            const twoDigits = s.slice(i - 1, i + 1);
            if (twoDigits >= "10" && twoDigits <= "26") {
                curr += downTwo;
            }

            // if neither yields combination, return 0
            if (curr == "0") {
                return 0;
            }

            // move rolling variables
            downTwo = downOne;
            downOne = curr;
        }

        return downOne;
    }
}