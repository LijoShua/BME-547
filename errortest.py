def hello():
    # try:
        # from my_calculator import sqrt
    # except ModuleNotFoundError:
        # from math import sqrt
        # print("My calculator module not available. Using default.")
    # answer = sqrt(n)
    # return answer
    a = 12345
    c = 1
    from warnings import warn
    warn("You are writing a not-so-good function")
    try:
        b = a/c
    except ZeroDivisionError:
        print("Cannot divide by zero. ")
    except TypeError:
        print("Cannot divide by a string. ")
    except Exception: # Not good programming practice
        print("Generic error encountered. ")
    else:
        return a/1
    # print(b)
    c = 0
    if c == 0:
        raise ZeroDivisionError("c is zero, and we cannot divide by zero")
    
def main():
    print(hello())

if __name__ == "__main__":
    main()
    