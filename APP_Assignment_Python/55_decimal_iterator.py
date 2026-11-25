class NumberIterator:
    def __init__(self, start=0.0, stop=1.0, step=0.25):
        self.current, self.stop, self.step = start, stop, step
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.stop + 1e-9: raise StopIteration
        value = round(self.current, 10)
        self.current += self.step
        return value

if __name__ == "__main__":
    for number in NumberIterator(): print(number)
