class my_class():
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return self.r*100
pass
dir = my_class(5)
print(dir.get_area())
