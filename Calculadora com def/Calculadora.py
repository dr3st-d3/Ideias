from Matematicabasica import soma, subtração, multiplicação, divisão

print("Bem vindo a calculadora básica!!!")

Operação = input("\n~~ Lista de Operações ~~ \n\n[1 - Soma] \n[2 - Subtração] \n[3 - Multiplicação] \n[4 - Divisão] \n\nSelecione sua operação: ")

a = float(input("\nDigite o primeiro valor: "))
b = float(input("\nDigite o segundo valor: "))

if Operação == ("1"):
    
    print("\nO Resultado da soma é: %.2f" %(soma(a, b)))

if Operação == ("2"):
    
    print("\nO Resultado da subtração é: %.2f" %(subtração(a, b)))

if Operação == ("3"):
    
    print("\nO Resultado da multiplicação é: %.2f" %(multiplicação(a, b)))

if Operação == ("4"):
    
    print("\nO Resultado da divisão é: %.2f" %(divisão(a, b)))

else:
    print("\nDigite uma Operação válida.")