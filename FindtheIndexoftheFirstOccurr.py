# 28. Find the Index of the First Occurrence in a String
# Easy
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 
'''
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''
# my solution(brutal force, O(n*m))
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        slic = len(needle)
        q = 0
        if slic > len(haystack):
            return -1
        while q <= len(haystack) - slic :
            p = 0
            for i in range(q, q + slic):
                if haystack[i] != needle[p]:
                    break
                else:
                    p += 1
            if p != slic:
                q += 1
            else:
                return q
        return -1

# neetcode solution 1(brutal force)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle):
                    return i
        return -1

# neetcode solution 1.5(brutal force & cheat in python)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1

# neetcode solution 2(KMP, elegant, O(n+m), O(m))
        