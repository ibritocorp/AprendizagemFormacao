"""
Crie um programa que leia o nome completo de uma pessoa e mostre o primeiro e último nome.
"""

nome = input('Digite o nome: ').strip().split()
print(f'Primeiro: {nome[0].capitalize()}\nÚltimo: {nome[len(nome) - 1].capitalize()}')
