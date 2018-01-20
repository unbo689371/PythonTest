def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError, ValueError):
        pass

    return False

print(is_number('foo'))
print(is_number('1'))
print(is_number('1.3'))
print(is_number('1.37'))
print(is_number('1e3'))
print(is_number('a'))
