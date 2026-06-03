class Solution {
    public int getSum(int a, int b) {
        // Loop runs until there are no more carries
        while (b != 0) {
            // calculate partial sum using XOR (addition without carries)
            int xorSum = a ^ b;

            // calculate the carries using AND, then shift left by 1
            int carry = (a & b) << 1;

            // update a to hold the sum, and b to hold the carries
            a = xorSum;
            b = carry;
        }

        return a;
    }
}