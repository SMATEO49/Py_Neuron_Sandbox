from math import tanh


class Cell:

    def __init__(self):
        self.weights = []
        self.inputs = []
        self.res = 0

    def set_weights(self, new_weights):
        self.weights = new_weights

    def set_inputs(self, inputs):
        self.inputs = inputs

    def response(self, typ):
        self.res = 0
        for i in range(len(self.inputs)):
            self.res += self.weights[i] * self.inputs[i]

        if typ == 'Linear':
            self.res = self.res
        elif typ == 'Tanh':
            self.res = tanh(self.res)
        elif typ == '0-1':
            if self.res > 0:
                self.res = 1
            else:
                self.res = 0
        elif typ == '0-x':
            if self.res > 0:
                self.res = self.res
            else:
                self.res = 0
        return self.res


w = [-1, -2, -1]
il = [3, 2, 1]
cell = Cell()
cell.set_weights(w)
cell.set_inputs(il)
odp = cell.response('Tanh')
print(odp)
