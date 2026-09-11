class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # Map digits to how many times they appear
        digits_to_count = {}
        for digit in digits:
            digits_to_count[digit] = digits_to_count.get(digit, 0) + 1

        res = 0
        for d1 in range(1, 10):  # Hundreds digit, no leading 0
            if d1 not in digits_to_count:  # Skip if not in given digits
                continue
            for d2 in range(10):  # Tens digit
                if d2 not in digits_to_count:  # Skip if not in given digits
                    continue
                for d3 in {0, 2, 4, 6, 8}:  # Ones digit, ensure its even
                    if d3 not in digits_to_count:  # SKip if not in given digits
                        continue
                    all_digits = {}
                    all_digits[d1] = all_digits.get(d1, 0) + 1
                    all_digits[d2] = all_digits.get(d2, 0) + 1
                    all_digits[d3] = all_digits.get(d3, 0) + 1
                    # We know all digits in all_digits can be compared with digits_to_count
                    if all(all_digits[d] <= digits_to_count[d] for d in all_digits):
                        res += 1

        return res
        
