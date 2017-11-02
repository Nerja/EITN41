__author__ = "Niklas Jönsson"

def luhn_test(card_number):
    return True

#function checkLuhn(string purportedCC) {
#     int sum := 0
#     int nDigits := length(purportedCC)
#     int parity := nDigits modulus 2
#     for i from 0 to nDigits - 1 {
#         int digit := integer(purportedCC[i])
#         if i modulus 2 = parity
#             digit := digit × 2
#             if digit > 9
#                 digit := digit - 9
#         sum := sum + digit
#     }
#     return (sum modulus 10) = 0
 #}
