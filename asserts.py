# def count_upper_case(message):
#     count = 0
#     for c in message:
#         if c.isupper():
#             count += 1
#     return count

# assert count_upper_case("") == 0, "Empty string"
# assert count_upper_case("A") == 1, "One upper case"
# assert count_upper_case("a") == 0, "One lower case"
# assert count_upper_case("£$%%^") == 0, "Special characters"
# assert count_upper_case("@") == 0, "Special @"

# print("All the tests passed")

def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("C") == 1, "Capital C"

print (count_upper_case(C))