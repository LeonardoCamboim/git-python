
idade = float(input("Idade do atleta: "))

if idade >= 5 and idade <= 7:
    print("Infantil A")
elif idade >= 8 and idade <= 10:
    print("Infantil B")
elif idade >= 11 and idade <= 13:
    print("Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Juvenil B")
elif idade >= 18:
    print("Senior")
else:
    print("O aluno não tem idade para competir")

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
if num1 > num2:
    resultado = num1 - num2
    print(resultado)
else:
    resultado = num2 - num1
    print(resultado)