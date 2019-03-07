def myrange(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    if len(args) == 2:
        start, stop, step = args[0], args[1], 1
    if len(args) == 3:
        start, stop, step = args[0], args[1], args[2]

    if len(args) == 0:
        raise TypeError("range expected 1 arguments, got 0")
    if len(args) > 3:
        raise TypeError("range expected at most 3 arguments, got {}".format(len(args)))

    try:
        start, stop, step = int(start), int(stop), int(step)
    except ValueError:
        raise TypeError("an integer is required")

    if step > 0:
        while start < stop:
            yield start
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step
    else:
        raise ValueError('range() arg 3 must not be zero')
