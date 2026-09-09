#googled solution

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Frequency map for characters we must satisfy
        target_counts = Counter(t)
        need = len(target_counts)
        have = 0

        window_counts = {}

        # Store result as (length, left_idx, right_idx)
        best_len = float("inf")
        best_window = (0, 0)

        left = 0

        # Expand the window with the right pointer
        for right, char in enumerate(s):
            # 1. Add incoming character to current window
            window_counts[char] = window_counts.get(char, 0) + 1

            # If this character just reached the exact required frequency, increment 'have'
            if (
                char in target_counts
                and window_counts[char] == target_counts[char]
            ):
                have += 1

            # 2. While window is valid, contract from the left to find the minimum
            while have == need:
                # Update best result if current window is smaller
                window_size = right - left + 1
                if window_size < best_len:
                    best_len = window_size
                    best_window = (left, right)

                # Pop left character
                left_char = s[left]
                window_counts[left_char] -= 1

                # If removing left_char causes us to fall below target count, decrement 'have'
                if (
                    left_char in target_counts
                    and window_counts[left_char] < target_counts[left_char]
                ):
                    have -= 1

                left += 1

        start, end = best_window
        return s[start : end + 1] if best_len != float("inf") else ""