def palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome
    :param value: A string
    :return: A boolean
    """
    result = True
    value_rev = value[::-1]
    if value != value_rev:
        result = False
    return result