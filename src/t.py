# should not report trailing-whitespace, missing-docstring, invalid-name
# should report bare-except
def divide(a, b): 

    try:
        result = a / b
    except:
        result = None

    return result
