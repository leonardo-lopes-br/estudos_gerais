from datetime import datetime, timedelta
from datas_br import DatasBR

hoje = datetime.today()
amanha = datetime.today() + timedelta(days=15, hours=9, minutes=15, seconds=53)
print(amanha - hoje)
