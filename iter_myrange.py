class MyRange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start, self.stop, self.step = 0, args[0], 1
        elif len(args) == 2:
            self.start, self.stop, self.step = args[0], args[1], 1
        elif len(args) == 3:
            self.start, self.stop, self.step = args[0], args[1], args[2]
        elif len(args) == 0:
            raise TypeError("range expected 1 arguments, got 0")
        else:
            raise TypeError("range expected at most 3 arguments, got {}".format(len(args)))
        try:
            self.start, self.stop, self.step = int(self.start), int(self.stop), int(self.step)
        except ValueError:
            raise TypeError("an integer is required")

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            while self.start < self.stop:
                current_value = self.start
                self.start += self.step
                return current_value
            else:
                raise StopIteration

        elif self.step < 0:
            while self.start > self.stop:
                current_value = self.start
                self.start += self.step
                return current_value
            else:
                raise StopIteration
        else:
            raise ValueError('range() arg 3 must not be zero')
