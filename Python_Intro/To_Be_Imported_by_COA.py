

class _Private:  # private classes by convention has a '_' in the start
    def __init__(self, name):
        self.name = name


class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):  # private methods by convention has a '_' in the start
        print('Hello')

    def display(self):
        print('Hi')
