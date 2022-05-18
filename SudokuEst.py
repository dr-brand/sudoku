
def validar_fila(grilla, valor, fila):
    for o in range(9):
        if grilla[fila][o] == valor:
            return False
    return True

def validar_columna(grilla, valor, columna):
    for o in range(9):
        if grilla[o][columna] == valor:
            return False
    return True

def validar_cuadrante(grilla, valor, fila, columna):
    rango_columna = columna - (columna % 3)
    rango_fila = fila - (fila % 3)
    for k in range(3):
        
        for l in range(3):
            if grilla[rango_fila + k][rango_columna + l] == valor:
                return False
    return True

def validar(grilla, valor, fila, columna):
   
    if not validar_fila(grilla, valor, fila):
        #print("valido fila")
        return False
    if not validar_columna(grilla, valor, columna):
        #print("valido columna")
        return False
    if not validar_cuadrante(grilla, valor, fila, columna):
        #print("valido cuadrante")
        return False
    #print(f"valido {valor}")
    return True
v=1
def sudoku_solver(grilla):
  
    for i in range(9):
        for j in range(9):
            if grilla[i][j] == 0:
                for v in range (1,10): 
                    if validar(grilla, v, i, j):
                        grilla[i][j] = v
                        if sudoku_solver(grilla):
                            return True
                        else:
                            grilla[i][j] = 0
                return False
    return True

def mostrar_grilla(grilla):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-------------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end = '')
            print(f"{grilla[i][j]}", end = '')
        print("\n", end = '')                                      
               
                
                    
        
        
      
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
    
    if sudoku_solver(grilla):
        print("Sudoku resuelto")
        mostrar_grilla(grilla)
    else:
        print("no posee solucion")
    