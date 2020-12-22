
def plus(value1: float, value2: float) -> float:
    if valid_float(value1) and valid_float(value2):
        return value1 + value2

def minus(value1: float, value2: float) -> float:
    if valid_float(value1) and valid_float(value2):
        return value1 - value2

def multiplication(value1: float, value2: float) -> float:
    if valid_float(value1) and valid_float(value2):
        return value1 * value2

def division(value1: float, value2: float) -> float:
    if valid_float(value1) and valid_float(value2) and valid_division(value2):
        return value1 / value2

def valid_float(n:float) -> bool:
    if isinstance(n, float):
        return True
    raise ValueError(f'Value {n} needs to be a valid number')

def valid_division (n: float) -> bool:
    if n != 0:
        return True
    raise ZeroDivisionError(f'Its "impossible" divide by zero!')
