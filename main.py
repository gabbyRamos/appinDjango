import requests


def menu():
    options = int(input("Deseja realizar uma nova consulta? \n1. Sim\n2. exit\n"))

    if options == 1:
        main()
    else:
        print("Saindo...")
        exit()


def main():
    print("########")
    print("#Consulta CeP")
    print('########')
    print()
    cep = input("Digite um cep para consulta: ")

    if len(cep) != 8:
        print("Quantidade de digitos invalida")
        menu()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    adress_data = request.json()

    if 'erro' not in adress_data:

        print('CEP: {}'.format(adress_data['cep']))
        print('Logradouro: {}'.format(adress_data['logradouro']))
        print('complemento: {}'.format(adress_data['complemento']))
        print('bairro: {}'.format(adress_data['bairro']))
        print('localidade: {}'.format(adress_data['localidade']))
        print('uf: {}'.format(adress_data['uf']))
        print('complemento: 06422 100{}'.format(adress_data['complemento']))
    else:
        print("{}: CEP invalido".format(cep))
        menu()


if __name__ == '__main__':
    main()



