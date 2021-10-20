from typing import Optional

def is_prime(n):
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
    assert find_all_superprimes([1, 2, 3]) == [2, 3]
    assert find_all_superprimes([173, 239, 173, 239, 100, 200, 5]) == [239, 239,5]
    assert find_all_superprimes([5]) == [5]
    assert find_all_superprimes([731, 5, 500, 23, 1000]) == [5, 23]
    assert find_all_superprimes([5, 7, 1, 2, 3, 233, 239, 137]) == [5, 7, 2, 3, 233, 239]


def test_is_superprime():
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
    assert find_smallest_number_having_given_last_digit(9, [1, 9, 29, 10, 5, 199]) == 9
    assert find_smallest_number_having_given_last_digit(7, [1, 9, 29, 10, 5, 199]) is None
    assert find_smallest_number_having_given_last_digit(0, [10, 0, 100, 200, 51410]) == 0


def test_find_smallest_number_in_list():
    assert find_smallest_number_in_list([1, 2, -5, 1000]) == -5
    assert find_smallest_number_in_list([100, 200, 5, 50, 2]) == 2
    assert find_smallest_number_in_list([1000000]) == 1000000
    assert find_smallest_number_in_list([]) is None

def test_find_numbers_with_given_last_digit():
    assert find_numbers_with_given_last_digit(9, [1, 9, 29, 10, 5, 199]) == [9, 29, 199]
    assert find_numbers_with_given_last_digit(7, [1, 9, 29, 10, 5, 199]) == []
    assert find_numbers_with_given_last_digit(0, [10, 0, 100, 200, 51410]) == [10, 0, 100, 200, 51410]


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


def test_find_negative_numbers():
    assert find_negative_integers([1, 2, -1, -2]) == [-1, -2]
    assert find_negative_integers([1, 2, 3]) == []
    assert find_negative_integers([-5000, -100]) == [-5000, -100]


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
    print("--------------------")
    print("0. EXIT")


def run_tests():
    test_find_negative_numbers()
    test_find_numbers_with_given_last_digit()
    test_find_smallest_number_in_list()
    test_find_smallest_number_having_given_last_digit()
    test_is_superprime()
    test_find_all_superprimes()
    pass


def main():
    """ Entry point for the program. """
    run_tests()
    ui_loop()


if __name__ == "__main__":
    main()
