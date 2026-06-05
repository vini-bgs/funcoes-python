# Filtrar Dados Acima de um Limite


def filtro(lista: list, corte: int) -> list:
    """
    Função retorna uma lista com valores maiores que o corte
    """
    # verifica se todos os valores da lista são números inteiros
    nova_lista = []
    for i in lista:
        try:
            n = int(i)
            if n > corte:
                nova_lista.append(n)

        except ValueError:
            raise ValueError(f"Atenção! O valor {i} não é válido.")

    return nova_lista


try:
    entrada = input("Entre com numeros separados por ',': ").split(",")

    corte = int(input("Qual o valor de corte? "))

    resultado = filtro(lista=entrada, corte=corte)
    print(resultado)

except ValueError as err:
    print(err)
