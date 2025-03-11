# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    c=''
    c=s[::-1]
    return c 
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    # TODO: Implement this function
    pass


def count_vowels(s: str) -> int:
  
    v="aeiou"
    m=v.upper()
    V=v+m
    a=0
    for i in range(len(s)):
        if s[i] in V:
            a+=1
    print('the number of vowels is',a)
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    # TODO: Implement this function
    pass


def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    a=s[::-1]
    if a==s :
        return True
    else:
        return False
    # TODO: Implement this function
    pass


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
        
    """
  a=s[0]
  cap=a.upper()+s[1::]
  return cap
    # TODO: Implement this function
    pass
