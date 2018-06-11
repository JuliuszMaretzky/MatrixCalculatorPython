import Operations

print("Witaj Użytkowniku!/nPobawmy się w operacje na macierzach:")
command=""
while command != "0":
    print("\nCo chcesz zrobić?")
    print("1. Dodawanie macierzy.")
    print("2. Odejmowanie macierzy.")
    print("3. Mnożenie macierzy przez liczbę.")
    print("4. Mnożenie dwóch macierzy.")
    print("5. Obliczanie wyznacznika macierzy.")
    print("0. Koniec zabawy.")

    command=input("Wybierz odpowiednią cyfrę: ")

    if(command=="1"):
        Operations.MatrixAddition()
    elif(command=="2"):
        Operations.MatrixSubtraction()
    elif(command=="3"):
        Operations.MatrixMultiplicationByNumber()
    elif(command=="4"):
        Operations.MatrixMultiplication()
    elif(command=="5"):
        Operations.MatrixDeterminant()
    elif(command=="0"):
        print("Do zobaczenia!")
        break
    else:
        print("\nNiepoprawna komenda. Spróbuj jeszcze raz.")
