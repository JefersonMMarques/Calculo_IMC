# Calcular o Indice de Massa Corporal:
#     Achar a formula e usar os dados fornecidos pelo usuario.
nome = input('Digite o seu nome: ')
massa = int(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = massa / altura ** 2
print(f'Olá {nome}, de acordo com sua altura e peso, seu IMC é de {imc:.2f}.')
