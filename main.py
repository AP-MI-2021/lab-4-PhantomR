from typing import Optional


def gcd2(x: int, y: int) -> int:
    """
    Finds the greatest common divisor of two numbers.

    Parameters
    ----------
    x, y: int
        The two numbers whose GCD we are trying to find.

    Returns
    -------
    int:
        The GCD of x and y.
    """
    # we use Euclid's subtraction-based algorithm
    # if the two numbers are the same, their GCD is their common value
    if x == y:
        return x

    # if the two numbers are distinct, we call recursively, changing only the
    # largest's value by subtracting the lower one from it
    if x > y:
        return gcd2(x - y, y)
    else:
        return gcd2(x, y - x)


def test_gcd2():
    assert gcd2(1, 2) == 1
    assert gcd2(2, 100) == 2
    assert gcd2(90, 30) == 30
    assert gcd2(7, 9) == 1


def gcd_list(lst: list[int]) -> int:
    """
    Finds the GCD of all the numbers in a given list of integers.

    Parameters
    ----------
    lst : list[int]
        The list containing the numbers whose GCD we are trying to find.

    Returns
    -------
    int:
        The GCD of all the numbers in the given list.

    """

    if len(lst) == 1:
        return lst[0]

    # we use the fact that gcd(a0,a2,...,an) = gcd(gcd(a0,..,a(n-1)), an)
    return gcd2(lst[-1], gcd_list(lst[:-1]))


def replace_positive_numbers_by_their_gcd(lst: list[int]) -> list[int]:
    """
    Returns a list where  all positive numbers in the given list have been replaced by their GCD.

    Parameters
    ----------
    lst : list[int]
        The list we are processing.

    Returns
    -------
    list[int]:
        A copy of the given list where all positive numbers have beeen replaced by their GCD.

    """

    positive_numbers = find_positive_integers(lst)
    gcd_of_positive_numbers = gcd_list(positive_numbers)
    result = []
    for element in lst:
        if element > 0:
            result.append(gcd_of_positive_numbers)
        else:
            result.append(element)

    return result


def test_replace_positive_numbers_by_their_gcd():
    assert replace_positive_numbers_by_their_gcd([1, 2, 3]) == [1, 1, 1]
    assert replace_positive_numbers_by_their_gcd([-1, -2, 100, 200, -5, 15]) == [-1, -2, 5, 5, -5, 5]


def replace_nonpositive_numbers_by_their_mirror_image(lst: list[int]) -> list[int]:
    """
    Returns a list where  all nonpositive numbers in the given list have been replaced by their mirror images.

    Parameters
    ----------
    lst : list[int]
        The list we are processing.

    Returns
    -------
    list[int]:
        A copy of the given list where all nonpositive numbers have beeen replaced by their mirror images.

    """
    result = []
    for element in lst:
        if element <= 0:
            # mirror the element
            mirrored_modulus = int(str(-element)[::-1])
            result.append(-mirrored_modulus)
        else:
            result.append(element)

    return result


def test_replace_nonpositive_numbers_by_their_mirror_images():
    assert replace_nonpositive_numbers_by_their_mirror_image([-1, -2, 0, 1, 2, 3]) == [-1, -2, 0, 1, 2,3]
    assert replace_nonpositive_numbers_by_their_mirror_image([-76, -2, 0, 100, 237, -34]) == [-67, -2, 0, 100, 237, -43]


def test_gcd_list():
    """
    Tests the gcd_list(list[int]) function.
    """
    assert gcd_list([1, 2]) == 1
    assert gcd_list([2, 100]) == 2
    assert gcd_list([90, 30]) == 30
    assert gcd_list([7, 9]) == 1
    assert gcd_list([20, 10, 100, 15]) == 5
    assert gcd_list([2, 3, 7, 9]) == 1


def is_prime(n: int) -> bool:
    """
    NOTE: This function was imported from my Lab2 homework. It was tested there.
    Tests whether an integer is a prime number.

    Parameters
    ----------
    n : int
        The natural number whose primality we want to test.

    Returns
    -------
        True if and only if n is a prime.
    """
    # 0 and 1 are not primes, by definition
    if (n == 0) or (n == 1):
        return False

    # 2 and 3 are primes
    if (n == 2) or (n ==3):
        return True

    # all even numbers > 2 are NOT primes
    if n % 2 == 0:
        return False

    # for odd numbers > 2, we only check odd divisors
    for d in range(3, (n // 2) + 1, 2):
        if n % d == 0:
          return False

    # no divisor was found, so the number must be a prime
    return True


def is_superprime(number: int) -> bool:
    """
    Determines if a given integer is a superprime, i.e the number and all its prefixes are primes.

    Parameters
    ----------
    number : int
        The number whose superprimality we are testing.

    Returns
    -------
    bool:
        True, if the give number is a superprime. False, otherwise.

    """
    while number > 0:
        if not is_prime(number):
            return False

        number = number // 10

    return True


def find_all_superprimes(lst: list[int]) -> list[int]:
    """
    Outputs a new list containing the superprimes in the given list.

    Parameters
    ----------
    lst : list[int]
        The list we are looking for superprimes in.

    Returns
    -------
    list[int]:
        The list of superprimes in the given list.

    """
    result = []
    for element in lst:
        if is_superprime(element):
            result.append(element)

    return result


def test_find_all_superprimes():
    """
    Tests the find_all_superprimes(list[int]) function.
    """
    assert find_all_superprimes([1, 2, 3]) == [2, 3]
    assert find_all_superprimes([173, 239, 173, 239, 100, 200, 5]) == [239, 239,5]
    assert find_all_superprimes([5]) == [5]
    assert find_all_superprimes([731, 5, 500, 23, 1000]) == [5, 23]
    assert find_all_superprimes([5, 7, 1, 2, 3, 233, 239, 137]) == [5, 7, 2, 3, 233, 239]


def test_is_superprime():
    """
    Tests the is_superprime(int) function.
    """
    assert not is_superprime(173)
    assert is_superprime(239)
    assert is_superprime(5)


def find_numbers_with_given_last_digit(digit: int, lst: list[int]) -> list[int]:
    """
    Finds all numbers in the given list having the given last digit.

    Parameters
    ----------
    digit : int
        The last digit we want our numbers to have.
    lst : list[int]
        The list of numbers we are searching.

    Returns
    -------
    list[int]:
        A list of all the numbers in the given list having the given last digit

    """
    result = []
    for number in lst:
        if number % 10 == digit:
            result.append(number)

    return result


def find_smallest_number_in_list(lst: list[int]) -> Optional[int]:
    """
    Given a list, finds the smallest number in it.

    Parameters
    ----------
    lst : list[int]
        The list whose minimum we are looking for.

    Returns
    -------
    Optional[int]:
        The smallest number in the given list, if it exists. None, if it does not exist.

    """
    # list is empty, so it does not have a minimum element
    if len(lst) == 0:
        return None

    minimum = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < minimum:
            minimum = lst[i]

    return minimum


def find_smallest_number_having_given_last_digit(digit: int, lst: list[int]) -> Optional[int]:
    """
    Finds the smallest number in the given list having the given last digit.

    Parameters
    ----------
    digit : int
        The last digit we want.
    lst : list[int]
        The list of numbers we are searching.

    Returns
    -------
    int:
        The smallest number in the list having the last digit we want, if it exists. None, if it does not exist.

    """
    numbers_with_given_last_digit = find_numbers_with_given_last_digit(digit, lst)
    smallest_number_with_given_last_digit = find_smallest_number_in_list(numbers_with_given_last_digit)
    return smallest_number_with_given_last_digit


def test_find_smallest_number_having_given_last_digit():
    """
    Tests the find_smallest_number_having_given_last_digit(int, list[int]) function.
    """
    assert find_smallest_number_having_given_last_digit(9, [1, 9, 29, 10, 5, 199]) == 9
    assert find_smallest_number_having_given_last_digit(7, [1, 9, 29, 10, 5, 199]) is None
    assert find_smallest_number_having_given_last_digit(0, [10, 0, 100, 200, 51410]) == 0


def test_find_smallest_number_in_list():
    """
    Tests the find_smallest_number_in_list(list[int]) function.
    """
    assert find_smallest_number_in_list([1, 2, -5, 1000]) == -5
    assert find_smallest_number_in_list([100, 200, 5, 50, 2]) == 2
    assert find_smallest_number_in_list([1000000]) == 1000000
    assert find_smallest_number_in_list([]) is None


def test_find_numbers_with_given_last_digit():
    """
    Tests the find_numbers_with_given_last_digit(int, list[int]) function.
    """
    assert find_numbers_with_given_last_digit(9, [1, 9, 29, 10, 5, 199]) == [9, 29, 199]
    assert find_numbers_with_given_last_digit(7, [1, 9, 29, 10, 5, 199]) == []
    assert find_numbers_with_given_last_digit(0, [10, 0, 100, 200, 51410]) == [10, 0, 100, 200, 51410]


def find_positive_integers(lst: list[int]) -> list[int]:
    """
    Finds positive numbers in the given list and returns them in a new list.

    Parameters
    ----------
    lst : list[int]
        The list in which we are looking for positive numbers.

    Returns
    -------
    list[int]
        The positive numbers found in the given list.

    """
    positive_numbers = []
    for element in lst:
        if element > 0:
            positive_numbers.append(element)

    return positive_numbers


def find_negative_integers(lst: list[int]) -> list[int]:
    """
    Finds negative numbers in the given list and returns them in a new list.

    Parameters
    ----------
    lst : list[int]
        The list in which we are looking for negative numbers.

    Returns
    -------
    list[int]
        The negative numbers found in the given list.

    """
    negative_numbers = []
    for element in lst:
        if element < 0:
            negative_numbers.append(element)

    return negative_numbers


def test_find_negative_integers():
    """
    Tests the find_negative_integers(list[int]) function.
    """
    assert find_negative_integers([1, 2, -1, -2]) == [-1, -2]
    assert find_negative_integers([1, 2, 3]) == []
    assert find_negative_integers([-5000, -100]) == [-5000, -100]


def test_find_positive_integers():
    """
    Tests the find_positive_integers(list[int]) function.
    """
    assert find_positive_integers([1, 2, -1, -2]) == [1, 2]
    assert find_positive_integers([1, 2, 3]) == [1, 2, 3]
    assert find_positive_integers([-5000, -100]) == []


def ui_process_read_list() -> list[int]:
    """
    Reads a sequence of integers separated by spaces from Standard Input, and converts it
    to a list of integers.

    Returns
    -------
    list[int]:
        The list of integers obtained from converting the user's input.
    """
    user_input = input("Input the elements of the list (integers) separated by spaces: ")
    list_of_strings = user_input.split(' ')
    list_of_ints = [int(element) for element in list_of_strings]
    return list_of_ints


def ui_read_command() -> int:
    """
    Reads an integer, representing a command number, from Standard Input.

    Returns
    -------
    int:
        The command number read.
    """
    return int(input("Please enter a command: "))


def ui_process_display_list(lst: list[int]):
    """
    Displays a list to Standard Output.

    Parameters
    ----------
    lst : list[int]
        The list to display.
    """
    print(lst)


def ui_process_find_negative_numbers(lst: list[int]):
    """
    Finde the negative numbers in the given list and outputs them to Standard Output.
    Parameters
    ----------
    lst : list[int]
        The list in which we are looking for negative numbers
    """
    negative_numbers = find_negative_integers(lst)
    ui_process_display_list(negative_numbers)


def ui_process_find_smallest_number_having_given_last_digit(lst: list[int]):
    """
    Reads a last digit from Standard Input, then outputs the smallest number in the given list having this last digit
    to Standard Output.

    Parameters
    ----------
    lst : list[int]
        The list we are searching.
    """

    last_digit = int(input("Input the last digit: "))
    smallest_number_with_given_last_digit = find_smallest_number_having_given_last_digit(last_digit, lst)
    print(smallest_number_with_given_last_digit)


def ui_process_find_all_superprimes(lst: list[int]):
    """
    Displays a list of all the superprimes in the given list to Standard Output.

    Parameters
    ----------
    lst : list[int]
        The list in which we are looking for superprimes.

    """
    superprimes = find_all_superprimes(lst)
    ui_process_display_list(superprimes)


def replace_positives_by_their_gcd_and_nonpositives_by_their_mirrored(lst: list[int]) -> list[int]:
    """
    Creates list based on the given list, where the positive numbers in the given list have been replaced by their
    GCD and nonpositives have been replaced by their mirror images.
    Parameters
    ----------
    lst : list[int]
        The original list.

    Returns
    -------
    list[int]:
        A list obtained from the given list, having the required replacements.

    """
    list_with_positives_replaced_by_gcd = replace_positive_numbers_by_their_gcd(lst)
    list_with_positives_replaced_by_gcd_and_nonpositives_replaced_by_mirrored = \
        replace_nonpositive_numbers_by_their_mirror_image(list_with_positives_replaced_by_gcd)
    return list_with_positives_replaced_by_gcd_and_nonpositives_replaced_by_mirrored


def test_replace_positives_by_their_gcd_and_nonpositives_by_their_mirrored():
    assert replace_positives_by_their_gcd_and_nonpositives_by_their_mirrored([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]
    assert replace_positives_by_their_gcd_and_nonpositives_by_their_mirrored([-765, -12, 24, -13, 144]) == [-567, -21, 24, -31, 24]


def ui_process_replace_positives_by_their_gcd_and_nonpositives_by_their_mirrored(lst: list[int]):
    """
    Displays a list based on the given list, where the positive numbers in the given list have been replaced by their
    GCD and nonpositives have been replaced by their mirror images.

    Parameters
    ----------
    lst : list[int]
        The source list.
    """
    result = replace_positives_by_their_gcd_and_nonpositives_by_their_mirrored(lst)
    ui_process_display_list(result)


def ui_process_command(command: int, lst: list[int]) -> (list[int], bool):
    """
    Receives a command number and processes it, eventually using the list lst.
    Returns the (possible modified) list and a bool telling whether an exit command was
    issued or not.

    Parameters
    ----------
    command : int
        The command to process, specified by a number.
    lst : list[int]
        The list used by some of the commands.

    Returns
    -------
    list[int]:
        The (possible modified) list.
    bool:
        True, if the command is an EXIT command; False, otherwise.
    """

    exit_command = False

    if command == 0:
        exit_command = True
    elif command == 1:
        lst = ui_process_read_list()
    elif command == 2:
        ui_process_display_list(lst)
    elif command == 3:
        ui_process_find_negative_numbers(lst)
    elif command == 4:
        ui_process_find_smallest_number_having_given_last_digit(lst)
    elif command == 5:
        ui_process_find_all_superprimes(lst)
    elif command == 6:
        ui_process_replace_positives_by_their_gcd_and_nonpositives_by_their_mirrored(lst)
    else:
        print("Invalid command. Please try again.")

    return lst, exit_command


def ui_loop():
    """ Reads and processes commands repeatedly until an EXIT command is received. """
    exit_command_was_received = False
    lst = []
    while not exit_command_was_received:
        ui_show_menu()
        command = ui_read_command()
        lst, exit_command_was_received = ui_process_command(command, lst)


def ui_show_menu():
    """ Displays a menu showing available commands. """
    print()
    print("Available commands:")
    print("--------------------")
    print("1. Read list")
    print("2. Display list")
    print("3. Find negative numbers in the list")
    print("4. Find the smallest number in the list having a given last digit")
    print("5. Find all superprimes in the list")
    print("6. Compute a list from the given list such that the positive numbers are replaced by their GCD and the "
          "nonpositives are replaced by their mirror images")
    print("--------------------")
    print("0. EXIT")


def run_tests():
    """
    Runs all tests.
    """
    test_find_negative_integers()
    test_find_positive_integers()
    test_find_numbers_with_given_last_digit()
    test_find_smallest_number_in_list()
    test_find_smallest_number_having_given_last_digit()
    test_is_superprime()
    test_find_all_superprimes()
    test_gcd2()
    test_gcd_list()
    test_replace_positive_numbers_by_their_gcd()
    test_replace_nonpositive_numbers_by_their_mirror_images()
    test_replace_positives_by_their_gcd_and_nonpositives_by_their_mirrored()

    print("[TESTS] All tests PASSED!!")


def main():
    """ Entry point for the program. """
    run_tests()
    ui_loop()


if __name__ == "__main__":
    main()
