class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        # Left boundary of our sliding window.
        l = 0

        res = 0

        # Keep track of the frequency of the most common
        # character in the current window.
        max_freq = 0
        
        for r in range(len(s)):
            # get the character at the right boundery
            char = s[r]
            # add the charater to the hashmap
            count[char] = count.get(char,0) + 1

            # Update the highest frequency we've seen
            # inside the current window.
            max_freq = max(max_freq, count[char])

            # Calculate how many characters we would need
            # to change to make the entire window the same.
            #
            # window size = right - left + 1
            # characters we need to change =
            # window size - most frequent character
            while (r - l + 1) - max_freq > k:

                # Remove the character at the left boundary
                # because we are shrinking the window.
                count[s[l]] -= 1

                # Move the left boundary one position to the right.
                l += 1

            # The current window is valid, so update the answer.
            res = max(res, r - l + 1)

        # Return the length of the longest valid window.
        return res




        