
multa = 193.50    
tarifa = 7.00    
placaA = []
velocidadeE = []

while True:
    placa = input(""+str(len(placaA)+1)+" Placa: ") 
    velocidade = str(input("Velocidade: "))

    if placa == '':
        break

    placaA = placaA+[placa]
    velocidadeE = velocidadeE+[velocidade]
    velocidadeE.sort()

print('\nO Carro Mais Rapido é')
x = velocidadeE.index(max(velocidadeE))
velocidadeE.sort()
print(f'Placa: {placaA[x]}')
print(f'Velocidade: {velocidadeE[-1]}')

print('\nMais Lento')
t = velocidadeE.index(min(velocidadeE))
velocidadeE.sort()
print(f'Placa: {placaA[t]}')
print(f'Velocidade: {velocidadeE[0]}')

print()

#Verificando a Velocidade médica do Veículo
qtdVeiculo = len(velocidadeE)
totalVelocidade = sum(int(x) for x in velocidadeE)
velocidadeMedia = str(totalVelocidade / qtdVeiculo)

print(f'Velocidade Média é: {velocidadeMedia} KM/h')

#veificando quantos veículos passaram acima de 40 KM/h
acima40 = 0
for num in velocidadeE: 
    
    if int(num) > int(40): 
        acima40 += 1
          
print(f'A Quantidade de {str(acima40)} Veículos passaram acima da média que é 40 KM/h') 

#somar total arrecadado por cada tarifa de 7,50
arrecadacaoTarifa = tarifa * qtdVeiculo
print(f'O Valor arrecadado é de R$ {arrecadacaoTarifa}') 

#somar total de multas arrecadado
arrecadacaoMulta = multa * acima40
print(f'O Valor arrecadado é de R$ {arrecadacaoMulta}') 