class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        long long original = x;
        long long reversed_num = 0;

        while (x > 0) {
            int digit = x % 10;
            reversed_num = reversed_num * 10 + digit;
            x /= 10;
        }

        return original == reversed_num;
    }
};