def fibonacci_sequence(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if n in fibonacci:
        return True
    else:
        return False

numero = int(input("Digite um numero: "))

if fibonacci_sequence(numero):
    print(f"O numero {numero} pertence a sequencia de Fibonacci.")
else:
    print(f"O numero {numero} nao pertence a sequencia de Fibonacci.")
