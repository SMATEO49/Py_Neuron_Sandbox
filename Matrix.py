class Matrix2:
    def __init__(self, a, b):
        self.x = b
        self.y = a
        self.matrix = []
        res = []
        for i in range(self.y):
            for j in range(self.x):
                res.append([0])
        self.matrix = res

    def ret(self, x, y):
        response = self.matrix[(y*self.x + x)]
        return response

    def ordinate(self, y):
        response = []
        for i in range(self.x):
            response.append(self.matrix[self.x * y + i])
        return response

    def abscissa(self, x):
        response = []
        for i in range(self.y):
            response.append(self.matrix[self.x * i + x])
        return response


kot = Matrix2(2, 2)
print(kot.abscissa(1))
