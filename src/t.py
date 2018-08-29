# should not report missing-docstring, invalid-name
# should report trailing-whitespace and bare-except
def divide(a, b): 

    try:
        result = a / b
    except:
        result = None

    return result
