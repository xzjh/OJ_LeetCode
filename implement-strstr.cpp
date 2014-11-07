class Solution {
public:
    int strStr(char *haystack, char *needle) {
        char *a = haystack, *b = needle, *str_base = haystack;
        for (;;)
            if (!*b)                return (int) (str_base - haystack);
            else if (!*a)           return -1;
            else if (*a++ != *b++)  { a = ++str_base; b = needle; }
    }
};
