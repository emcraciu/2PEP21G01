def my_area_function(length: int, width: int):
    if type(length) not in (int, float) or type(width) not in (int, float):
        raise TypeError
    if length < 0 or width < 0:
        raise ValueError
    return length * width
