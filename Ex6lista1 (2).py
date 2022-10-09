tamanho = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade de Internet (MBps): '))
print('Tempo aproximado de download: %.2f Minutos ' %((tamanho / velocidade) / 60))