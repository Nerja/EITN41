import format_converter as fc

__author__ = "Marcus Rodan"

if __name__ == "__main__":
    print("Question 1: {}".format(fc.int_to_hex(2897)))
    print("Question 2: {}".format(fc.hash_int(2897, 4)))
    print("Question 3: {}".format(fc.hex_to_int("0123456789abcdef")))
    print("Question 4: {}".format(fc.hex_to_int(fc.hash_int(fc.hex_to_int("0123456789abcdef"),8))))

