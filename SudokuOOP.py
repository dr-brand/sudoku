class Sudoku:
   #inicializa un tablero o grilla vacia de 9x9
    def __init__(self):
        self.grilla =  [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

    #verifica si el digito esta en la columna
    def isInColumn(self, grilla, count, j):
        for k in range(9):
            if self.grilla[k][j] ==  count:
                return True
        return False

    #verifica si el digito esta en la fila
    def isInRow(self, grilla, count, i):
        for l in range(9):
            if self.grilla[i][l] ==  count:
                return True
        return False

    #verifica si el digito esta en el cuadrante 3x3
    def isInCuadrant(self, grilla, count, j, i):
        for l in range((i-i%3),((i-i%3)+3)):
            for k in range((j-j%3),((j-j%3)+3)):
                if self.grilla[k][l] ==  count:
                    return True
        return False

    #Agrupa los 3 metodos anteriores para un codigo mas bonito
    def isDigit(self, grilla, count, j, i):
        if not (self.isInColumn(self.grilla, count, j) or self.isInRow(self.grilla, count, i) or self.isInCuadrant(self.grilla, count, i, j)):
            return True
        return False

    #Procedimiento de resolucion
    def solver(self):
        for i in range(9): #recorre filas
            for j in range(9):  #recorre columnas
                if self.grilla[i][j] == 0 :
                    for count in range(1,10):
                        if self.isDigit(grilla, count, j, i):
                            self.grilla[i][j] = count 
                            if self.solver():
                                return self.grilla
                            else:
                                self.grilla[i][j] = 0
                    return False   
        return True       

    #Imprime la grilla en formato Sudoku en Consola
    def printgrilla(self):
        for i in range(9):
            for j in range(9):
                print(self.grilla[i][j],end="")
                if ((j+1) % 3 == 0) and ((j+1)/3 != 3):
                    print("|", end="")
            print("")
            if ((i+1) % 3 == 0) and (i != 0) and ((i+1)/3 != 3):
                print("------------")
        print("\n")

    def tieneSolucion(self):
        if self.solver():
            print("La solucion es:")
            self.printgrilla()
        else:
            print("No tiene solucion!!")
                    

if __name__ == '__main__':
    grilla = [[3,2,0,4,0,6,0,0,5],
        [0,0,6,9,2,0,0,0,0],
        [0,1,0,0,0,0,0,0,0],
        [4,0,1,3,0,0,8,2,0],
        [5,0,0,0,0,0,0,9,0],
        [0,0,2,0,0,0,0,0,4],
        [0,0,3,0,8,0,0,0,1],
        [0,5,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,3,6,0]]
    n = Sudoku()
    n.printgrilla()
    n.grilla = grilla
    n.tieneSolucion()


