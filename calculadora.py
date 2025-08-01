def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def main():
    print("=== Calculadora Python ===")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Escolha a operação (+, -, *, /): ").strip()

        if operacao == "+":
            resultado = soma(num1, num2)
        elif operacao == "-":
            resultado = subtracao(num1, num2)
        elif operacao == "*":
            resultado = multiplicacao(num1, num2)
        elif operacao == "/":
            resultado = divisao(num1, num2)
        else:
            resultado = "Operação inválida!"

        print(f"Resultado: {resultado}")
    
    except ValueError:
        print("Erro: Digite apenas números válidos.")

if __name__ == "__main__":
    main()
