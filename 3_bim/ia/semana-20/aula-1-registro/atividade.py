import pandas as pd
import numpy as np

# Criando um DataFrame com dados fictícios
data = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Idade': [23, 35, 45, 32, 28],
    'Salário': [5000, 6000, 7000, 8000, 9000]
}

df = pd.DataFrame(data)

# Exibindo o DataFrame
print("DataFrame original:")
print(df)

# Adicionando uma nova coluna 'Imposto' (20% do salário)
df['Imposto'] = df['Salário'] * 0.20

# Calculando a média da idade
media_idade = np.mean(df['Idade'])
print(f"\nMédia da Idade: {media_idade}")

# Filtrando dados - mostrando apenas pessoas com salário acima de 6000
salario_acima_6000 = df[df['Salário'] > 6000]

print("\nPessoas com salário acima de 6000:")
print(salario_acima_6000)
