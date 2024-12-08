def calcular_media():
    try:
        qtd_alunos = int(input("Digite a quantidade de alunos na turma: "))
        soma_notas = 0

        for i in range(1, qtd_alunos + 1):
            nota = float(input(f"Digite a nota do aluno {i}: "))
            soma_notas += nota

        media = soma_notas / qtd_alunos
        print(f"\nA média das notas da turma é: {media:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")

# Executa o programa
calcular_media()
