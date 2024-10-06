print("********************Welcome to Python Calculator********************")

more_calculations = True

while more_calculations:
    Operand = input("Enter Operation You Want To Perform \nAdd(+) Subtract(-) Multiply(*) Divide(/) Power(**)\n")
    m = float(input("Enter First Number: "))
    n = float(input("Enter Second Number: "))

    def addition(m, n):
        return m + n
    def subtraction(m, n):
        return m - n
    def multiplication(m, n):
        return m * n
    def division(m, n):
        return m / n
    def power(m,n):
        return m ** n

    Operations = {'+': addition, '-': subtraction, '*': multiplication, '/': division, '**': power}

    Calculation_function = Operations[Operand]
    Answer = Calculation_function(m, n)

    print(f" {m} {Operand} {n} = {Answer}")

    Choice = input("Want to Calculate More! Yes or No  \n")
    if Choice in "noNo":
        more_calculations = False
