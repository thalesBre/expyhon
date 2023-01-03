from typing import Tuple


def calcular_primos_e_divisoes(divisivel: int) -> Tuple[str, int]:
    """Escreva aqui em baixo a sua solução"""
    primos, divisoes = '', 0
    for n in range(1, divisivel + 1):
        (divisoes := 1)
        if eh_primo(n):
            primos += f'{str(n)}, '
    primos = primos.removesuffix(', ')

    return primos, divisoes