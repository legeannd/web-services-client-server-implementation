import requests

api_url = 'http://localhost:5000'

while True:
    print("Escolha uma opção: (0 - sair)")
    print("1 - Listar produtos")
    print("2 - Listar produto por ID")
    print("3 - Adicionar produto")
    print("4 - Alterar produto")
    print("5 - Remover produto")
    opc = input()
    if opc == "0":
        break
    
    elif opc == "1":

        response = requests.get(api_url+"/products")
        print("Produtos:")
        for i in response.json()['products']:
            print("#####################################")
            print("\n")
            print("Nome: " + i['name'])
            print("Valor: " + str(i['value']))
            print("Quantidade: " + str(i['quantity']))
            print("ID: " + i['id'])
            print("\n")
    
    elif opc == "2":
        id = input("Digite o ID do produto buscado\n")
        response = requests.get(api_url+"/products/"+id)
        if "error" in response.json(): 
            print("ID inválido")
        else:
            product = response.json()['product']
            print("#####################################")
            print("\n")
            print("Nome: " + product['name'])
            print("Valor: " + str(product['value']))
            print("Quantidade: " + str(product['quantity']))
            print("ID: " + product['id'])
            print("\n")

    elif opc == "3":
        name = input("Digite o nome do produto\n")
        value = int(input("Digite o valor do produto\n"))
        quantity  = int(input("Digite a quantidade do produto\n"))
        product = {
            "name": name,
            "value": value,
            "quantity": quantity
        }
        response = requests.post(api_url+"/products", json=product)
        product_created = response.json()['product']
        print("#####################################")
        print("Produto criado!")
        print("\n")
        print("Nome: " + product_created['name'])
        print("Valor: " + str(product_created['value']))
        print("Quantidade: " + str(product_created['quantity']))
        print("ID: " + product_created['id'])
        print("\n")
    
    elif opc == "4":
        id = input("Digite o ID do produto que deseja alterar\n")
        name = input("Digite o nome do produto\n")
        value = int(input("Digite o valor do produto\n"))
        quantity  = int(input("Digite a quantidade do produto\n"))
        product = {
            "name": name,
            "value": value,
            "quantity": quantity
        }
        response = requests.put(api_url+"/products/"+id, json=product)
        if "error" in response.json(): 
            print("ID inválido")
        else:
            product_created = response.json()['product']
            print("#####################################")
            print("Produto criado!")
            print("\n")
            print("Nome: " + product_created['name'])
            print("Valor: " + str(product_created['value']))
            print("Quantidade: " + str(product_created['quantity']))
            print("ID: " + product_created['id'])
            print("\n")

    elif opc == "5":
        id = input("Digite o ID do produto a ser deletado\n")
        response = requests.delete(api_url+"/products/"+id)
        if "error" in response.json(): 
            print("ID inválido")
        else:
            result = response.json()['result']
            if result == True:
                print("#####################################")
                print("\n")
                print("O produto com id "+id+" foi deletado com sucesso")
                print("\n")
            else: 
                print("Não foi possível deletar o produto")

    else:
        print("Opção inválida")