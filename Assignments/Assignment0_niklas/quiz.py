import convert as c
if __name__ == "__main__":
    #Take the integer 2897 and treat it as 4 bytes (big endian).
    #Give a hexadecimal string representation of the integer (written as an 8-byte string)
    print(c.int_byte_hex(2897, 4) )

    #Take the integer 2897 and treat it as 4 bytes (big endian). Hash this array using SHA-1
    #and provide the result as a hex-string. The output of SHA-1 is 20 bytes,
    #so your answer should be a 40-byte string.
    print(c.int_byte_hash_hex(2897, 4))

    #Take the 16-byte string '0123456789abcdef' and treat it as an 8-byte array of bytes.
    #Give the integer representation of the byte array.
    #print(c.bytearray2int ( c.hex2bytearray("0123456789abcdef") ) )
    print(c.hex_byte_int("0123456789abcdef"))
    #Take the 16-byte string '0123456789abcdef' and treat it as an 8-byte array of bytes.
    #Hash the byte array with SHA-1 and convert the answer to an integer. Provide the integer.
    print(c.hex_byte_hash_int("0123456789abcdef"))
