
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
         return '\n'.join([' '.join(['%d\t' % i for i in row]) for row in self.matrix])

    def size(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        return("rows = {0}, cols = {1}".format(rows,cols))

    def transpose(self):
        return '\n'.join([' '.join(['%d\t' % (self.matrix[i][j]) for i in range(0, len(self.matrix))]) for j in range(0,len(self.matrix[0]))])

    def __add__(self, second_matrix):
        if (type(second_matrix) == int or type(second_matrix) == float):
            return '\n'.join([' '.join(['%d\t' % (i + second_matrix) for i in row]) for row in self.matrix])

        if (self.size() == second_matrix.size()):
            return '\n'.join([' '.join(['%d\t' % (self.matrix[j][i] + second_matrix.matrix[j][i]) for i in range(0, len(self.matrix[0]))]) for j in range(0,len(self.matrix))])

    def __sub__(self, second_matrix):
        if (type(second_matrix) == int or type(second_matrix) == float):
            return '\n'.join([' '.join(['%d\t' % (i - second_matrix) for i in row]) for row in self.matrix])

        if (self.size() == second_matrix.size()):
            return '\n'.join([' '.join(['%d\t' % (self.matrix[j][i] - second_matrix.matrix[j][i]) for i in range(0, len(self.matrix[0]))]) for j in range(0,len(self.matrix))])

    def __mul__(self, second_matrix):
        if (type(second_matrix) == int or type(second_matrix) == float):
            return '\n'.join([' '.join(['%d\t' % (i * second_matrix) for i in row]) for row in self.matrix])

        if (len(self.matrix[0]) == len(second_matrix.matrix)):
            #print(1)
            itog = [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip(*second_matrix.matrix)] for row_a in self.matrix]
            return '\n'.join([' '.join(['%d\t' % i for i in row]) for row in itog])

    def det(self):
        if (len(self.matrix) != len(self.matrix[0])): return None
        AM = self.matrix

        for fd in range(len(self.matrix)):
            for i in range(fd+1,len(self.matrix)):
                if AM[fd][fd] == 0:
                    AM[fd][fd] == 1.0e-18
                crScaler = AM[i][fd] / AM[fd][fd]
                for j in range(len(self.matrix)):
                    AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

        product = 1.0
        for i in range(len(self.matrix)):
            product *= AM[i][i]

        return product

a = Matrix([[1,2,3], [4,5,6], [7,8,9]])
b = Matrix([[3,2,1], [6,5,4], [9,8,7]])
c = Matrix([[3,2,1], [6,5,4]])

print("\n A = \n")
print(a, "\n")
print("size A =  ", a.size(), "\n")
print("B = \n")
print(b, "\n")
print("size B =  ", b.size(), "\n")
print("C = \n")
print(c, "\n")
print("size C =  ", c.size(), "\n")
print("A + 5 = \n")
print(a + 5, "\n")
print("A + B = \n")
print(a + b, "\n")
print("A - 1 = \n")
print(a - 1, "\n")
print("A - B = \n")
print(a - b, "\n")
print("A * 5 = \n")
print(a * 5, "\n")
print("C * B = \n")
print(c * b, "\n")
print("A^T = \n")
print(a.transpose(), "\n")
print("C^T = \n")
print(c.transpose(), "\n")
print("det(A) = ", a.det(), "\n")
print("det(B) = ", b.det(), "\n")
print("det(C) = ", c.det(), "\n", "\n", "\n")
