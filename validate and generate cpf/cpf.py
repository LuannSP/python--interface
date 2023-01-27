from random import randint
import re

def generateCpf() -> str:
    cpf = str(randint(100000000, 999999999))
    newCpf = _returnCpf(cpf)
    return newCpf

def validateCpf(cpf: str) -> bool:
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    newCpf = cpf[:-2]

    if cpf == _returnCpf(newCpf):
        return True
    return False

def _returnCpf(newCpf: str) -> str:
    digit = 0
    for i, c in enumerate(newCpf[::-1], 2):
        digit += i*int(c)
    else:
        digit = 11 - (digit % 11)
        result = 0 if digit > 9 else digit
        newCpf += str(result)
        if len(newCpf) == 11:
            return newCpf
        return _returnCpf(newCpf)
