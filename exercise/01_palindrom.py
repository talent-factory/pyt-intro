def is_palindrome(s):
    """
    Check if the given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring spaces and case.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.

    Examples:
    >>> is_palindrome("A man a plan a canal Panama")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("Was it a car or a cat I saw")
    True
    >>> is_palindrome("No lemon, no melon")
    True
    """

    s = s.replace(" ", "").lower()
    return s == s[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
