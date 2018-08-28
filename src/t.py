# should not report bare-except and others
# should report trailing-whitespace
def divide(a, b): 

    try:
        result = a / b
    except:
        result = None

    return result