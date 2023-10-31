"""
Calcula a raiz digital de um número não negativo.

Args: 
n (int): Número inteiro não negativo.

Returns:
int: O dígito único resultante após a aplicação do processo de soma recursiva.

"""

def digital_root(n):

    if n < 10:
        return n
    else:
        sum_digits = sum(int(digit) for digit in str(n))
        return digital_root(sum_digits)


# Testes unitários
def test_digital_root():
    assert digital_root(16) == 7

def test_zero_root():
    assert digital_root(0) != 4

def test_negative_root():
    assert digital_root(-34234) == -34234

def test_float_root():
    assert digital_root(3.5) == 3.5


if __name__ == '__main__':
    test_digital_root()
    test_zero_root()
    test_negative_root()
    test_float_root()