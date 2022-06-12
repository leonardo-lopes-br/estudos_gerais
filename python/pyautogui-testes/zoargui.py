import pyautogui as p
from time import sleep
p.PAUSE = 0.3
p.alert('Começando')
p.press('winleft')
p.write('Brave')
p.press('enter')
sleep(1)
p.moveTo(333,313) # posição do zap
p.click()
sleep(6)
p.moveTo(100,465) #primeiro resultado
p.click()
p.write('Oi')
sleep(0.5)
p.press('enter')
for i in range(0,5):
    p.write('gostoso')
    sleep(0.2)
    p.press('enter')
p.alert('Acabou')
