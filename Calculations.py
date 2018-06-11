#funkcja dodająca dwie macierze
def Add(matrix1, matrix2):
    sum=[]
    for r in range(len(matrix1)):
        sum.append([])
        for c in range(len(matrix1[0])):
            sum[r].append(matrix1[r][c]+matrix2[r][c])
    return sum


#funkcja odejmująca drugą macierz od pierwszej
def Subtract(matrix1, matrix2):
    difference=[]
    for r in range(len(matrix1)):
        difference.append([])
        for c in range(len(matrix1[0])):
            difference[r].append(matrix1[r][c]-matrix2[r][c])
    return difference


#funkcja mnożąca macierz przez liczbę
def MultiplyByNumber(matrix,number):

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c]*=number

    return matrix


#funkcja mnożąca dwie macierze
def Multiply(matrix1, matrix2):
    product=[]

    for r in range(len(matrix1)):
        product.append([])
        for c in range(len(matrix2[0])):
            product[r].append(0)
            for m in range(len(matrix2)):
                product[r][c]+=matrix1[r][m]*matrix2[m][c]

    return product


#funkcja obliczająca wyznacznik macierzy
def Determinant(matrix):

    sign=0

    for p in range(1,len(matrix)):
        swapper=p

        while matrix[p-1][p-1]==0:
            for k in range(len(matrix)):
                matrix[p-1][k],matrix[swapper][k]=matrix[swapper][k],matrix[p-1][k]
            sign+=1
            swapper+=1
            if swapper==len(matrix):
                break

        if matrix[p-1][p-1]==0:
            break

        for i in range(p,len(matrix)):
            multiplier=matrix[i][p-1]/matrix[p-1][p-1]

            for j in range(p-1,len(matrix)):
                matrix[i][j]=matrix[i][j]-multiplier*matrix[p-1][j]

    det=1
    for ind in range(len(matrix)):
        det=det*matrix[ind][ind]

    return (-1)**sign*det

