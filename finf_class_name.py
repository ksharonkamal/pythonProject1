class Number:
    def __init__(self, number):
        self.number = number

n1 = Number(1)
print(n1.__class__)
print(n1.__class__.__name__)