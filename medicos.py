import json

#Cadastro de médico
def cadastro_medico():
    dados = {}
    dados['name'] = input('Nome: ')
    dados['email'] = input('Email:')
    # dados['phone'] = input('Telefone: ')
    # dados['cell'] = input('Celular: ')
    # dados['crm'] = input('CRM: ')
    # dados['rg'] = input('RG: ')
    # dados['cpf'] = input('CPF: ')
    # dados['number'] = input('Endereço: ')
    # dados['specialization'] = input('Especialização: ')
    # dados['address'] = input('número: ')
    # dados['hood']= input('Bairro: ') 
    # dados['city']= input('Cidade: ')
    # dados['estado'] = input('UF: ')
    # dados['plano'] = input('Plano de saúde: ')
    print('Cadastrado com sucesso! \n\n')
    return dados

def listar_medicos():
    with open('dados_medicos.json',) as dados_medicos:
        lista_medicos = json.load(dados_medicos)
        print('medicos: \n')
        for medico in lista_medicos:
            print(medico['name'])
    print('-'*20)

def menu_medicos():
    while True:
        print('''1 - Cadastrar novo medico
2 - Listar medicos
3 - Sair
        ''')
        opcao = int(input('Selecione uma opção: \n'))
        if opcao == 1:
            try:
                with open('dados_medicos.json') as medicos:
                    antigos_medicos = json.load(medicos)
                with open('dados_medicos.json', mode='w') as dados_medicos:
                    antigos_medicos.append(cadastro_medico())
                    novos_medicos = json.dumps(antigos_medicos)
                    dados_medicos.write(novos_medicos)
            except:
                with open('dados_medicos.json', mode='w') as dados_medicos:
                    novos_medicos = []
                    novos_medicos.append(cadastro_medico())
                    medicos = json.dumps(novos_medicos)
                    dados_medicos.write(medicos)

        elif opcao == 2:
            listar_medicos()
        elif opcao == 3:
            break
        else:
            print("Opção inválida!")