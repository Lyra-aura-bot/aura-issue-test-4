def divide(x, y):
    """
    Returns the integer division of x by y.
    BUG: when y == 0, this returns None instead of raising an error.
    """
    if y == 0:
        raise ValueError('Division by zero is not allowed')
    return x // y