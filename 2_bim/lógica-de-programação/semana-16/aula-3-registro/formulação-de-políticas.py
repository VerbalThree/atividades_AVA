qualidade_do_ar = int(input("Qual é a qualidade do ar? (0 - 100)\n"))

if qualidade_do_ar >= 80:
    print("A qualidade do ar está excelente. Mantenha as políticas atuais.\n")
elif qualidade_do_ar >= 60:
    print("A qualidade do ar está boa. Considere políticas moderadas de melhoria.\n")
else:
    print("A qualidade do ar está ruim. Implemente políticas rigorosas de melhoria.\n")