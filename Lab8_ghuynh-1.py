"""
UPC Validator
Gaven Huynh
This program will ask the user for a 12-digit UPC-A code and calculate the correct check digit.
It should also determine if the UPC is valid.
March 5, 2026
"""

def find_UPC(first11: str) -> int:

    odd_num = 0
    even_num = 0

    for num in range(len(first11)):
        digit: int = int(first11[num])

        if num % 2 == 0:
            odd_num += digit
        else:
            even_num += digit
        
        total: int = (odd_num * 3) + even_num
        
        check_digit: int = (10 - (total % 10)) % 10

        return check_digit
    
upc: str

while True:
    upc = input("Please enter a 12-digit UPC: ")

    if len(upc) == 12 and upc.isdigit():
        break
    else:
        print("Invalid input. Please enter exactly 12 numeric digits.")

first11: str = upc[:11]
given_digit: int = int(upc[11])

print(f"The first 11 digits of the UPC-A are '{first11}'.")
print(f"The check digit is '{given_digit}'.")

print("Calculating. . .")

expected_digit: int = find_UPC(first11)