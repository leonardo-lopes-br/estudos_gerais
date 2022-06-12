import requests


class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.validar_CEP(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def validar_CEP(self, cep):
        return len(cep) == 8

    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acessar_via_cep(self):
        url = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
        dados = url.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )


meu_cep = BuscaEndereco(13563265)
bairro, cidade, uf = meu_cep.acessar_via_cep()
print(bairro)
print(cidade)
print(uf)
