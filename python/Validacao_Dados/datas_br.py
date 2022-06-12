from datetime import datetime


class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                 'Outubro', 'Novembro', 'Dezembro']
        return meses[self.momento_cadastro.month - 1]

    def dia_cadastro(self):
        dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
        return dias[self.momento_cadastro.day - 1]

    def format_data(self):
        return self.momento_cadastro.strftime('%d/%m/%Y %H:%M')

    def tempo_cadastro(self):
        return datetime.today() - self.momento_cadastro
