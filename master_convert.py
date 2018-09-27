"""function switcher.  dec->bin; bin->dec; eventually dec->hex; hex->dec
gather user input"""

import binary_converter
import hexadecimal_converter

CONTINUE = True
print("Number Conversion Utility")
while CONTINUE:


    print("MENU:".center(23))
    print("1 - Decimal to Binary\n2 - Binary to Decimal\n3 - Decimal to hexadecimal\n4 - Hexadecimal to Decimal")
    CHOICE = input("Option:_")
    if CHOICE == "1":
        YOUR_NUMBER = float(input("Enter a Decimal:_"))
        YOUR_OUTPUT = binary_converter.convert_dec_to_bin(YOUR_NUMBER)
        YOUR_TYPE = "binary"
    elif CHOICE == "2":
        YOUR_NUMBER = float(input("Enter a Binary:_"))
        YOUR_OUTPUT = binary_converter.convert_bin_to_dec(YOUR_NUMBER)
        YOUR_TYPE = "decimal"
    elif CHOICE == "3":
        YOUR_NUMBER = float(input("Enter a Decimal:_"))
        YOUR_OUTPUT = hexadecimal_converter.convert_dec_to_hex(YOUR_NUMBER)
        YOUR_TYPE = "hexadecimal"
    elif CHOICE == "4":
        YOUR_NUMBER = input("Enter a Hexadecimal:_")
        YOUR_OUTPUT = hexadecimal_converter.convert_hex_to_dec(YOUR_NUMBER)
        YOUR_TYPE = "decimal"
    else:
        pass

    print(YOUR_NUMBER, " in ", YOUR_TYPE, " is ", YOUR_OUTPUT)
    if input("Continue: [Y]es/[N]o ").casefold() == "N".casefold():
        CONTINUE = False
