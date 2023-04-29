import math


def calc(x: float) -> str:
    """Suninjuly's robot captcha"""
    return str(math.log(abs(12 * math.sin(x))))
