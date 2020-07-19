def luhn_algorithm(code):

    """Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers.

    1. From the rightmost digit and moving left, double the value of every second digit.
    If the result of this doubling operation is greater than 9, then add the digits of the result
    or, alternatively, the same final result can be found by subtracting 9 from that result.

    2. Take the sum of all the digits.

    3. If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula;
    otherwise it is not valid."""

    list_of_digit = [int(i) for i in code if i.isdigit()]
    list_of_digit.reverse()
    odd_sum = sum(list_of_digit[::2])
    even_sum = 0
    for i in range(len(list_of_digit)):
        if i % 2 != 0:
            even_str = str(list_of_digit[i] * 2)
            for j in range(len(even_str)):
                even_sum += int(even_str[j])
    if (odd_sum + even_sum) % 10 == 0:
        #print("Verification passed: ", code)
        return True
    else:
        #print("Verification failed: ", code)
        return False


def main():
    test_list = ['1234 8765 2345 1234', '4561 2612 1234 5467', '4561 2612 1234 5464', '5536 0800 1149 6167',
                 '4276 5500 5423 1868', '1234 5678 9000 4321', '4242 4242 4242 4242', '4222 2222 2222 2223']
    for i in test_list
        luhn_algorithm(i


if __name__ == "__main__":
    main()