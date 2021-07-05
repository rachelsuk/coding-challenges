class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_rom={
            1:"I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        nums = str(num)
        result = ""
        multiplier = 1
        for digit in nums[::-1]:
            digit = int(digit)
            number = digit*multiplier
            if digit < 4:
                rom = int_to_rom[multiplier]*digit
            elif 5 < digit < 9:
                rom = int_to_rom[5*multiplier]+int_to_rom[multiplier]*(digit-5)
            else:
                rom = int_to_rom[number]
            multiplier *= 10
            result = rom + result
        return result