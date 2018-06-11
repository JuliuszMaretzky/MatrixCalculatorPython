import Calculations


#wczytywanie wymiarów macierzy
def MatrixDimensions():

    isOK=False
    while isOK==False:
        try:
            rows=int(input("\nPodaj liczbę wierszy macierzy: "))
            isOK=True
        except ValueError:
            print("Niepoprawna wartość!")

    isOK = False
    while isOK == False:
        try:
            columns=int(input("Podaj liczbę kolumn macierzy: "))
            isOK = True
        except ValueError:
            print("Niepoprawna wartość!")

    return [rows,columns]


#wczytywanie wymiarów macierzy do mnożenia
def MultiplyMatrixDimensions():

    isOK = False
    while isOK == False:
        try:
            firstEdge=int(input("\nPodaj liczbę wierszy pierwszej macierzy: "))
            isOK = True
        except ValueError:
            print("Niepoprawna wartość!")

    isOK = False
    while isOK == False:
        try:
            middleEdge=int(input("Podaj liczbę kolumny pierwszej macierzy (wierszy drugiej macierzy): "))
            isOK = True
        except ValueError:
            print("Niepoprawna wartość!")

    isOK = False
    while isOK == False:
            try:
                lastEdge=int(input("Podaj liczbę kolumn drugiej macierzy: "))
                isOK = True
            except ValueError:
                print("Niepoprawna wartość!")

    return [firstEdge, middleEdge, lastEdge]


#wczytanie wymiaru macierzy kwadratowej (wyznacznik)
def SquareMatrixDimension():

    isOK=False
    while isOK == False:
        try:
            dimension=int(input("\nPodaj wymiar macierzy: "))
            isOK = True
        except ValueError:
            print("Niepoprawna wartość!")

    return [dimension, dimension]


#wczytywanie macierzy "z ręki"
def LoadFromHand(dimensions, which):
    matrix=[]
    print()
    for r in range(dimensions[0]):
        matrix.append([])
        for c in range(dimensions[1]):
            isOK = False
            while isOK==False:
                try:
                    matrix[r].append(float(input("Podaj wyraz ["+str(r)+"]["+str(c)+"] "+which+" macierzy: ")))
                    isOK=True
                except ValueError:
                    print("Niepoprawna wartość!")

    for r in range(dimensions[0]):
        print(matrix[r])
    print()

    return matrix


#moduł dodawania macierzy
def MatrixAddition():
    dimensions=MatrixDimensions()

    matrix1=LoadFromHand(dimensions, "pierwszej")
    matrix2=LoadFromHand(dimensions, "drugiej")

    sum=Calculations.Add(matrix1,matrix2)
    print("Wynik dodawania: \n")
    for r in range(dimensions[0]):
        print(sum[r])


#moduł odejmowania macierzy
def MatrixSubtraction():
    dimensions=MatrixDimensions()

    matrix1=LoadFromHand(dimensions, "pierwszej")
    matrix2=LoadFromHand(dimensions, "drugiej")

    difference=Calculations.Subtract(matrix1,matrix2)
    print("Wynik odejmowania: \n")
    for r in range(dimensions[0]):
        print(difference[r])


#moduł mnożenia macierzy przez liczbę
def MatrixMultiplicationByNumber():
    dimensions=MatrixDimensions()

    matrix1=LoadFromHand(dimensions, "")

    isOK=False
    while isOK==False:
        try:
            number=float(input("Wybierz liczbę, przez którą chcesz pomnożyć macierz: "))
            isOK=True
        except TypeError:
            print("To nie jest liczba!")

    numberProduct=Calculations.MultiplyByNumber(matrix1,number)
    print("\nWynik mnożenia przez liczbę: \n")
    for r in range(dimensions[0]):
        print(numberProduct[r])


#moduł mnożenia dwóch macierzy
def MatrixMultiplication():
    dimensions=MultiplyMatrixDimensions()
    dimensions1=[dimensions[0], dimensions[1]]
    dimensions2=[dimensions[1],dimensions[2]]

    matrix1=LoadFromHand(dimensions1,"pierwszej")
    matrix2=LoadFromHand(dimensions2,"drugiej")

    product=Calculations.Multiply(matrix1, matrix2)

    print("Wynik mnożenia dwóch macierzy: \n")
    for r in range(dimensions[0]):
        print(product[r])


#moduł obliczania wyznacznika macierzy
def MatrixDeterminant():
    dimensions=SquareMatrixDimension()

    matrix=LoadFromHand(dimensions,"")

    print("Wyznacznik macierzy wynosi "+str(Calculations.Determinant(matrix)))

