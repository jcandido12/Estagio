def verificar_letra_a(texto):
    
    count_a_min = texto.co('a')
    count_a_mai = texto.count('A')
    total_a = count_a_min + count_a_mai

    if total_a > 0:
        print(f"A letra 'a' ocorre {total_a} vezes no texto.")
    else:
        print("A letra 'a' não foi encontrada no texto.")


texto = input("Digite uma string: ")
verificar_letra_a(texto)
