def add_integer(a, b=98):
    """Function that returns integer addtion of a and b.

    Raises a TypeError if either a or b is a non-integer."""

    if (not isintance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isintance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) +int(b))
