matrixData = [
    [1,1,1,1],
    [0,0,0,1],
    [0,0,0,1],
    [0,0,0,1],
]

print("[1] ClosuresOfRelations")
print("[2] PropertiesOfRelations")
selectType = int(input())
textWantInput = input('If You Won To Input Matrix y/n :').lower()

if textWantInput == 'y':
    try:
        sizeMtx = int(input('Size Matrix: '))
        newMtx = []
        for row in range(sizeMtx):
            rowData = []
            for col in range(sizeMtx):
                rowData.append(int(input(f"value at row: {row} col: {col} Value 0 or 1: ")))
            newMtx.append(rowData)
        matrixData = newMtx
    except ValueError:
        print('is not Number int')

def are_matrices_equal(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True

def boolean_matrix_multiply(matrix1, matrix2):
    size = len(matrix1)
    result = [[0] * size for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] |= matrix1[i][k] & matrix2[k][j]
    
    return result

class ClosuresOfRelations():
    def __init__(self, matrix):
        self.matrix = matrix
        self.node_count = len(matrix)


    def get_in_node(self, num_node):
        data = []
        for row in range(len(self.matrix)):
            if self.matrix[row][num_node] == 1:
                data.append(row)
        return data
    
    def get_out_node(self, num_node):
        return self.matrix[num_node]
    
    def debugMatrix(self):
        print('---- RESULT ----')
        for row in self.matrix:
            print(" ".join(map(str, row)))
    
    def reflexive(self):
        for i in range(len(self.matrix)):
            self.matrix[i][i] = 1
        print('--> Use Reflexive')

    def symmetric(self):
        for row in range(len(self.matrix)):
            for col in range(row + 1, len(self.matrix[row])):
                if self.matrix[row][col] == 1:
                    self.matrix[col][row] = 1

        print('--> Use Symmetric')

    def transitive(self, debug = False):
        for node_index in range(self.node_count):
            node_in = self.get_in_node(node_index)
            node_out = self.get_out_node(node_index)
            
            if debug:
                print(f'------ W{node_index + 1} -----')
                
            for index_in, in_value in enumerate(node_in):
                if in_value == 1:
                    for index_out, out_value in enumerate(node_out):
                        if out_value == 1:
                            self.matrix[index_in][index_out] = 1


        print('--> Use Transitive')

    def equivalence(self):
        self.reflexive()
        self.symmetric()
        self.transitive()

class PropertiesOfRelations():
    def __init__(self, matrix):
        self.matrix = matrix
        self.sizeMatrix = len(matrix)

    def is_identity_diagonal(self, custom_num = 1):
        count_ref = 0
        for i in range(len(self.matrix)):
            if self.matrix[i][i] == custom_num:
                count_ref += 1
                
        return count_ref == self.sizeMatrix
    def is_reflexive(self):        
        return self.is_identity_diagonal()
    
    def is_irreflexive(self):
        return self.is_identity_diagonal(custom_num = 0)
    
    def is_symmetric(self):
        for row in range(len(self.matrix)):
            for col in range(row + 1, len(self.matrix[row])):
                if self.matrix[row][col] == 1 and self.matrix[col][row] != 1:
                    return False
        return True

    def is_antisymmetric(self):
        for row in range(len(self.matrix)):
            for col in range(row + 1, len(self.matrix[row])):
                if self.matrix[row][col] == 1 and self.matrix[col][row] == 1:
                    return False
        return True
    
    def is_asymmetric(self):
        for row in range(len(self.matrix)):
            for col in range(row + 1, len(self.matrix[row])):
                if (self.matrix[row][col] == 1 and self.matrix[col][row] == 1) or self.matrix[row][row] == 1:
                    return False
        return True
    
    def is_transitive(self):
        if are_matrices_equal(boolean_matrix_multiply(self.matrix, self.matrix), self.matrix):
            return True
        Closures = ClosuresOfRelations(self.matrix)
        for node_index in range(Closures.node_count):
            node_in = Closures.get_in_node(node_index)
            node_out = Closures.get_out_node(node_index)
                
            for index_in, in_value in enumerate(node_in):
                if in_value == 1:
                    for index_out, out_value in enumerate(node_out):
                        if out_value == 1:
                            if (Closures.matrix[index_in][index_out] != 1):
                                return False
        return True
    
    def is_equivalence(self):
        if self.is_reflexive() and self.is_symmetric() and self.is_transitive():
            return True
        return False
    

relation_classes = {1: ClosuresOfRelations, 2: PropertiesOfRelations}
MTX = relation_classes.get(selectType, PropertiesOfRelations)(matrixData)
if selectType == 1:
    commentFnc = input('Enter if y need (r, s, t): ').split(' ')
    for cmd in commentFnc:
        if cmd == 'r':
            MTX.reflexive()       
        if cmd == 's':
            MTX.symmetric()
        if cmd == 't':
            MTX.transitive()
    MTX.debugMatrix()
else:
    print("Identity Diagonal: ", MTX.is_identity_diagonal())
    print("is Reflexive : ", MTX.is_reflexive())
    print("is Ireflexive : ", MTX.is_reflexive())
    print("is Symmetric : ", MTX.is_symmetric())
    print("is Antisymmetric : ", MTX.is_antisymmetric())
    print("is Asymmetric : ", MTX.is_asymmetric())
    print("is Transitive : ", MTX.is_transitive())
    print("is Equivalence : ", MTX.is_equivalence())