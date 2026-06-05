# Calcular a média de valores


def media_valores_lista(lista: list) -> float:
    """
    Função retorna a média dos valores de uma lista.
    Caso um valor da lista não seja numérico retorna um ValueError
    """
    valores_convertidos = []

    for i in lista:
        try:
            valores_convertidos.append(float(i))

        except ValueError:
            raise ValueError(
                f"O valor {i} da lista não é válido. \n"
                "Utilize apenas números e '.' como seperador decimal."
            )

    media = sum(valores_convertidos) / len(valores_convertidos)

    return media


lista = input("Entre com uma lista de números separados por ',': ").split(",")

try:
    resultado = media_valores_lista(lista=lista)
    print(resultado)

except ValueError as err:
    print(f"{err}")
