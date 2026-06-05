# Filtrar Dados Acima de um Limite


def filtro(lista: list, corte: int) -> list:
    """
    Função retorna uma lista com valores maiores que o corte
    """
    # verifica se todos os valores da lista são números inteiros
    nova_lista = []
    for i in lista:
        try:
            nova_lista.append(int(i))

        except ValueError as err:
            raise ValueError(err)

    lista_filtrada = []
    for n in nova_lista:
        if n > corte:
            lista_filtrada.append(n)

    return lista_filtrada


entrada = input("Entre com numeros separados por ',': ")

try:
    resultado = filtro(entrada, 2)
    print(resultado)

except ValueError as err:
    print({err})
