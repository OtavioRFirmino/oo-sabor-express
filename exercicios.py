#Exercicio 1
"""class Musica:
    nome = ''
    artista = ''
    duracao = float

musica_Ignite = Musica()
musica_Ignite.nome = 'Ignite'
musica_Ignite.artista = 'Alan Walker'
musica_Ignite.duracao = 2.35

print(vars(musica_Ignite))"""

#Exercicio 2
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]
print (restaurante_praca.ativo)