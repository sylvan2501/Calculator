class Coordinator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinator(self.x+other.x, self.y+other.y)

    def __mul__(self, other):
        return Coordinator(self.x * other.x, self.y * other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __call__(self, *args, **kwargs):
        print('I was called')


