import sys


def tracefunc(frame, event, arg):
    if event == 'return' and frame.f_locals:
        print(f'function: {frame.f_code.co_name},',
              f'local_vars: {list(frame.f_locals.keys())}')
    return tracefunc


def foo():
    friends = ["Bob", "Tom"]
    for f in friends:
        print(f"Hi {f}")
    return len(friends)


sys.settrace(tracefunc)
number_friends = foo()
