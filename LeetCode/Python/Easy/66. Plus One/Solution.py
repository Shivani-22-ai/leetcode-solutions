def convert_to_list(i):
    digit = []
    while i>0:
        digit.append(i%10)
        i = i//10
    return digit

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        i = ''.join(digits)
        i = int(i)
        i = i + 1
        digits = convert_to_list(i)
        return digits[::-1]

        