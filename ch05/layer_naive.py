class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        return out

    def backward(self, d_out):
        dx = d_out * self.y
        dy = d_out * self.x

        return dx, dy

class AddLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x + y
        return out

    def backward(self, d_out):
        dx = d_out * 1
        dy = d_out * 1
        return dx, dy
