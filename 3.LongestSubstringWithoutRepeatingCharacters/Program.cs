using System.Collections;

namespace _3.LongestSubstringWithoutRepeatingCharacters
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string inputString = "abcabcbb";
            int longestSubstringLength = Solution.LengthOfLongestSubstring(inputString);
            Console.WriteLine($"The length of the longest substring without repeating characters is: {longestSubstringLength}");
        }
    }

    public class Solution
    {
        public static int LengthOfLongestSubstring(string s)
        {
            int longest = 0;
            int left = 0;
            Dictionary<char, int> hashTable = new Dictionary<char, int>();

            for (var right = 0; right < s.Length; right++)
            {
                var current = s[right];
                if (!hashTable.ContainsKey(current))
                {
                    hashTable[current] = right;
                }
                else
                {
                    left = Math.Max(left, hashTable[current] + 1);
                    hashTable[current] = right;
                }

                longest = Math.Max(longest, right - left + 1);
            }

            return longest;
        }
    }
}
