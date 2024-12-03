class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
re=rectangle(10,10)
print("area=",re.area())
