# RESPOSTA:

"""
2. O código anterior teve alguns erros. Como por exemplo, quando o código verificava uma letra, ele uma letra minúscula, e não maiúscula.

3. Acredito que podemos fazer esse código de uma forma mais inteligente, utilizando array.
"""

letra = (input("Digite uma letra:\n"))
letra = letra.upper()

if letra == 'A':
    print("Abacaxi")
elif letra == 'B':
    print("Banana")
elif letra == 'C':
    print("Cachorro")
elif letra == 'D':
    print("Damasco")
elif letra == 'E':
    print("Elefante")
elif letra == 'F':
    print("Fuji")
elif letra == 'G':
    print("Galinha")
elif letra == 'H':
    print("Hortelã")
elif letra == 'I':
    print("Iguana")
elif letra == 'J':
    print("Jabuticaba")
elif letra == 'K':
    print("Kiwi")
elif letra == 'L':
    print("Leão")
elif letra == 'M':
    print("Macaco")
elif letra == 'N':
    print("Nectarina")
elif letra == 'O':
    print("Onça")
elif letra == 'P':
    print("Panda")
elif letra == 'Q':
    print("Quati")
elif letra == 'R':
    print("Romã")
elif letra == 'S':
    print("Sapoti")
elif letra == 'T':
    print("Tangerina")
elif letra == 'U':
    print("Uva")
elif letra == 'V':
    print("Vaca")
elif letra == 'W':
    print("Wampi")
elif letra == 'X':
    print("Xixá")
elif letra == 'Y':
    print("Yuzu")
elif letra == 'Z':
    print("Zebra")
else:
    print("Letra inválida. Digite uma letra do alfabeto.")
