def isiterable(obj):
    try:
        obj = iter(obj)
    except:
        return False
    else:
        return True


if __name__ == "__main__":
    a = [1, 2]
    b = 3
    print(f"'a' is {'iterable' if isiterable(a) else 'not iterable'}")
    print(f"'b' is {'iterable' if isiterable(b) else 'not iterable'}")
