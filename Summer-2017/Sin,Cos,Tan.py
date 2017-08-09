import math

opposite=(int(input("Please enter the Length of the Opposite Side")))
adjacent=(int(input("Please enter the Length of the Adjacent Side")))
hypotenuse=(int(input("Please enter the Length of the Hypotenuse Side")))

menu=input("Sin OR Cos OR Tan???")

if menu == "Sin":
    sin = opposite/hypotenuse
    print(sin)

elif menu == "Cos":
    cos = adjacent/hypotenuse
    print(cos)

elif menu == "Tan":
    tan = opposite/adjacent
    print(tan)
