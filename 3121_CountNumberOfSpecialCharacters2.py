class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Map each uppercase character to its first index/occurrence
        # Map each lowercase character to its last index/occurrence
        seen = {}
        for i, c in enumerate(word):  # enumerate gives (index, element) pairs
            if c.isupper() and c not in seen:  # Ensures first uppercase character chosen
                seen[c] = i
            elif c.islower():
                seen[c] = i

        # Now do the checking
        count = 0
        for c in seen:
            # Check that lowercase characters in seen appear before uppercase equivalents
            if c.islower() and c.upper() in seen and seen[c] < seen[c.upper()]:
                count += 1

        return count
