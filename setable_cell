class Cell:
    def __init__(self, lenght):
        self.weights = [0] * (lenght + 1)
        self.inputs = [0] * lenght
        self.semi_res = 0
        self.full_res = 0
    def set_weights(self, new_weights):
        for i in range(lenght + 1):
            self.weights[i] = new_weights[i]

    def inputs(self, inputs):
        for i in range(lenght):
            self.inputs[i] = inputs[i]

    def semi_res(self):
        self.semi_res = self.weights[lenght]
        for i in range(lenght):
            self.semi_res += self.weights[i] * self.inputs[i]

        return self.semi_res

    def full_res(self):
        self.semi_res = self.weights[lenght]
        for i in range(lenght):
            self.semi_res += self.weights[i] * self.inputs[i]

        if self.semi_res > 0 :
            self.full_res = 1
        else:
            self.full_res = 0
        return self.full_res
