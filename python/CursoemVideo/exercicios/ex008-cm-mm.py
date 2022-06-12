v = float(input('Digite um valor em metros: '))
km = v/1000
hem = v/100
dam = v/10
dm = v*10
cm = v*100
mm = v*1000
print('O valor {:.2f}m em decímetros é: {:.0f}dm'.format(v,dm))
print('O valor {:.2f}m em centímetros é: {:.0f}cm'.format(v,cm))
print('O valor {:.2f}m em milímetros é: {:.0f}mm'.format(v,mm))
print('O valor {:.2f}m em decâmetros é: {}dam'.format(v,dam))
print('O valor {:.2f}m em hectômetros é: {}hem'.format(v,hem))
print('O valor {:.2f}m em quilômetros é: {}km'.format(v,km))