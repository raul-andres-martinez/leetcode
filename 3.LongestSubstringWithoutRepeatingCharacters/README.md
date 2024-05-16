# Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

## Solution

For this algorithm, I chose the sliding window technique, along with a hash table.

The sliding window algorithm utilizes two pointers to track the current candidate for the longest substring, along with a hash table to keep track of the currently evaluated character and the index where it was last seen. 

I used a 'current' variable, pointing to the character at the current right pointer index. This variable is used as a key in the hash table, defining the character and its last seen index. Both the left and right pointers start at the 0 index. 

As we iterate through the string, the right pointer increases to the next index, while the left one is only updated when we find a duplicated character. When a duplicated character appears, we move the left pointer just to the next index from the found character, checking which index is bigger: the current left or the next index of the last-seen character's index element. 

This movement creates a new window, making the previous one the current longest and creating a new candidate. We need to update the index value of the current element in the hash table; that way, we can know the last index that this item was seen. After that, we update the 'longest' variable, looking for the larger value: the actual longest or the difference between the right and left pointers.

Time and Space complexity = O(n)