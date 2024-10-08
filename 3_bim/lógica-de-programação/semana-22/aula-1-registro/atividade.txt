num_fun = int(input("Digite o seu número de funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_por_hora = float(input("Digite o quanto recebe por hora:"))

salario = horas_trabalhadas * valor_por_hora

print(f"\nO seu número de funcionário: {num_fun}\nO seu salário: {salario:.2f}\n")