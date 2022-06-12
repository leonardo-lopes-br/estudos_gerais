import re


class TelefonesBr:
    def __init__(self, telefone):
        telefone = str(telefone)
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número incorreto!')

    def valida_telefone(self, telefone):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        return len(re.findall(padrao, telefone)) > 0

    def format_numero(self):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self.numero)
        codigo_country = resposta.group(1) if resposta.group(1) else '55'
        return f'+{codigo_country}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'

    def __str__(self):
        return self.format_numero()

