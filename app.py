from modelos.restaurante import Restaurante

restaurante_brasil = Restaurante('Brasil', 'Brasileira')
restaurante_bankai = Restaurante('Bankai', 'Japonesa')
restaurante_chichi = Restaurante('Chichi', 'Chilena')
restaurante_brasil.receber_avaliacao('Otavio', 7)
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()