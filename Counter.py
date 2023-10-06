class Counter:
    def __init__(self):
        self.value = 0
        self.opened = False

    def __enter__(self):
        self.opened = True
        return self

    def add(self):
        self.value += 1
        self.opened = False

    def __exit__(self, exc_type, exc_value, traceback):
        if self.opened == True:
            raise ValueError("Вы не заполнели поля")