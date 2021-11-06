def fibonacci(fin: float) -> float:
    """
    build a classic fibonacci function - No RECURSION
    """
    prev = 1
    two_prev = -1
    for i in range(0, fin + 1):
        current = prev + two_prev
        two_prev = prev
        prev = current
    return current