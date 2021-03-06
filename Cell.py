from math import tanh


class Cell:

    def __init__(self):
        self.weight = []

    def n_weight(self, new_weight):
        self.weight = new_weight

    def n_response(self, new_input, typ):
        response = 0
        for i in range(len(new_input)):
            response += self.weight[i] * new_input[i]
        if typ == '0-1':
            if response > 0:
                response = 0
            else:
                response = 1
        elif typ == '0-x':
            if response < 0:
                response = 0
        elif typ == 'tanh':
            response = tanh(response)
        return response


w = [1, 2, 1]
il = [3, 2, 1]
kot = Cell()
kot.n_weight(w)
odp = kot.n_response(il, 'tanh')
print(odp)
