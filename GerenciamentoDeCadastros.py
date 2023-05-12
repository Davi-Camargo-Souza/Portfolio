# DAVI CAMARGO DE SOUZA - ATIVIDADE SOMATIVA 2 - SEMANA 8
# RACIOCINIO COMPUTACIONAL

# Importei o json
import json

# Fiz uma função para escrever o json e utilizar ela para gravar os novos dados depois.
def escrever_json(file,nome):
    with open(nome+'.json','w') as f:
        json.dump(file,f)
        f.close()

# Essa função além de ler o json e gravar em uma váriavel, também é responsável pela chamada da função escrever_json na primeira vez em que o programa é aberto por conta do except.        
def ler_json(nome):
    try:
        with open(nome+'.json','r') as f:
            arquivo = json.load(f)
            f.close()
            return arquivo
    except FileNotFoundError: # Caso o arquivo n exista, é retornado uma lista vazia
        file = [] # Lista vazia que vai ser usada para criar o json
        return file


# Função que exibe o menu principal e faz a chamada da função redirecionar pra redirecionar o usuário pro menu escolhido.
def menu_inicial():
        while True: # O while True aqui opera pra sempre retornar a esse menu após sair dos outros. A menos que seja escolhido a opção SAIR, no caso a 6.
            print('\nPUC - MENU PRINCIPAL')
            # Lista das opções de menus:
            opcoes = ['Estudantes',
                    'Professores',
                    'Disciplinas',
                    'Turmas',
                    'Matrículas',
                    'Sair']
            # Estrutura for pra imprimir essas opções:
            i = 1 # O i começa em 1 pra ser o índice da escolha.
            for opcao in opcoes:
                print(f'[{i}] {opcao}')
                i += 1 # A cada passada o i é somado a 1.
            try: # O try aqui funciona pra evitar o erro do programa tentar converter texto para inteiro.
                op = int(input('Digite a opção desejada: '))
                if 1 <= op <= 5: # Se for a opção digitada for menor ou igual a 1 e menor ou igual a 5:
                    redirecionar(op) # Chama a função que redireciona o usuário para o menu especificado, passando como parâmetro a op, que seria como a identificação do menu.
                elif op == 6: # Se a opção digitada for 6 o loop é quebrado e o programa encerra.
                    print('\nEncerrando.')
                    break
                else: # Se não:
                    print('Opção inválida, tente novamente\n')
            except ValueError: # Se ocorrer erro de converter texto para inteiro:
                # Imprime essa mensagem e e pede pro usuário digitar novamente.
                print('Opção inválida, tente novamente\n')

# Função que redireciona o usuário para o menu escolhido (op).           
def redirecionar(op):
    while True: # O while True está aqui para que o menu seja sempre exibido, a menos que o usuário digite a opção 5 (voltar a o menu principal).
        nome = nomes(op) # O nome é obtido pela chamada da função nomes. Ela retorna o nome do menu em que o usuário está.
        print(f'\n{nome.upper()} - MENU') # Imprime o nome do menu seguido de '- MENU'
        mostrar_opcoes() # Mostra as opções possíveis.
        # Chama a função perguntas_acoes que redireciona o usuário para o menu da ação escolhida.
        if perguntas_acoes(op) == 5: # Caso a função retorne 5, o loop infinito é quebrado e o programa volta ao menu principal.
            break                

# Função que exibe as opções de ações a serem realizadas.
def mostrar_opcoes():    
    opcoes = ['Incluir',
            'Listar',
            'Atualizar',
            'Excluir',
            'Menu principal']
    # Mesma lógica de exibição do menu principal.
    i = 1
    for opcao in opcoes:
        print(f'[{i}] {opcao}')
        i += 1

# Função que redireciona o usuário para o menu da ação escolhida.
def perguntas_acoes(menu): # menu é a referência de qual menu o usuário veio.
    resp = perguntas() # Chama a função perguntas.7
    # Se a opção escolhida for _, chama a função __ passando menu como parâmetro:
    if resp == 1: 
        incluir(menu) 
    elif resp == 2: 
        listagem(menu) 
    elif resp == 3:
        atualizacao(menu)
    elif resp == 4:
        exclusao(menu) 
    # Se a opção escolhida for 5:
    elif resp == 5: 
        return resp # retorna resp para a linha 59 e o programa volta ao menu principal.
    
# Função que realiza o tratamento de exceção da opção desejada dentro do menu. Verificando se a opção é válida (de 5 opções), e se é o valor digitado é um inteiro.
# Ela é chamada após a escolha do menu (estudantes,professores,disciplinas etc.) lá na linha 67.
def perguntas():
    while True: # Loop infinito que só encerra quando o usúario digita um inteiro que seja uma opção válida do menu.
        try:
            op = int(input('Digite a opção desejada: '))
            if 1 <= op <= 5:
                break
            else:
                print('Opção inválida, tente novamente')
        except ValueError:
            print('Opção inválida, tente novamente')
    return op

# Função que retorna nomes, que são usados em frases, indíces, cabeçalhos, na abertura de arquivos json e na gravação de json.
def nomes(menu): # Usa o menu de onde o usuário veio como parâmetro.
    if menu == 1:
        nome = 'estudantes'
    elif menu == 2:
        nome = 'professores'
    elif menu == 3:
        nome = 'disciplinas'
    elif menu == 4:
        nome = 'turmas'
    elif menu == 5:
        nome = 'matriculas'
    return nome

# função de inclusão de cadastros.
def incluir(menu): # Usa o menu de onde o usuário veio como parâmetro.
    while True: # Loop para que o usuário possa incluir outros cadastros sem precisar voltar ao respectivo menu de escolhas.
        nome = nomes(menu) # nome vai receber o nome do menu.
        print(f'\n{nome.upper()} - INCLUSÃO') # {nome do menu} - inclusão
        tabela = ler_json(nome) # Abrindo a respectiva tabela e a armazenando em uma váriavel para que possamos adicionar mais cadastros
        cod = codigo_excecoes(nome) # Chama a função que realiza a pergunta do código.    
         # Chama a função checagem_duplicata, que verifica se já tem um cadastro com aquele código, se retornar True, mostra uma mensagem.  
        if checagem_duplicata(cod,tabela,nome):
                print(f'\nCódigo de {nome} já cadastrado, cadastre outro. ')
        else: # Se não, realiza as perguntas do cadastro:
            if menu in [1,2]: # Se o menu for 1 ou 2: (estudantes ou professores):
                # Atribuindo um titulo conforme o menu, para que a mensagem seja melhor explicada.
                if menu == 1:
                    titulo = 'estudante'
                elif menu == 2:
                    titulo = 'professor'
                # Usei strip e o title para tirar os espaços e ficar visualmente mais agradável ao listar.
                nomecadastro = str(input(f'Digite o nome do {titulo}: ')).strip().title()
                while True:
                    cpf = str(input(f'Digite o CPF do {titulo}: '))
                    # Verificando se o cpf é válido (se tem 11 caracteres):
                    if len(cpf) == 11:
                        break
                    elif len(cpf) < 11 or len(cpf) > 11:
                        print('CPF inválido, tente novamente, dessa vez utilizando um com 11 caracteres.')
                # Confere se já não tem um cadastro com aquele cpf, para evitar duplicatas.
                if checagem_duplicata(cpf,tabela,nome):
                    print(f'\nCPF já cadastrado, cadastre outro.')
                else:
                    # Atribui os dados fornecidos a um dicionario que é adicionado no fim da respectiva tabela.
                    dados = {'código':cod,'nome':nomecadastro,'cpf':cpf}
                    tabela.append(dados)
                    # Grava a tabela, com o mesmo nome, assim sobrescrevendo a anterior e mantendo ela atualizada.
                    escrever_json(tabela,nome)
                    print('\nCadastro concluído com sucesso')
            # Inclusão de disciplinas
            
#---------------------------------------------(mesma lógica de inclusão)------------------------------------------------------#  
            # Inclusão de disciplinas          
            elif menu == 3:
                    nomecadastro = str(input(f'Digite o nome da {nome[:-1]}: ')).strip().title()
                    dados = {'código':cod,'nome':nomecadastro}
                    tabela.append(dados)
                    escrever_json(tabela,nome)
                    print('\nCadastro concluído com sucesso')
            # Inclusão de turmas       
            elif menu == 4:
                    cod_professor = codigo_excecoes('professor')
                    # Chama a função validacao, que valida se o código de professor fornecido, é realmente de um professor cadastrado:
                    if validacao(cod_professor,"professores"): # Se retornar True, é porque não é correspondente a nenhum professor.
                        print('\nCódigo de professor não encontrado. Tente novamente.')
                    else:
                        cod_disciplina = codigo_excecoes('disciplina')
                        if validacao(cod_disciplina,'disciplinas'): # Mesma lógica da validação de professor.
                            print('\nCódigo de disciplina não encontrado.\n'
                                'Tente novamente.')
                        else:
                            dados = {'código':cod,'codprof':cod_professor,'coddisc':cod_disciplina}
                            tabela.append(dados)
                            escrever_json(tabela,nome)
                            print('\nCadastro concluído com sucesso')
            # Inclusão de matrículas
            elif menu == 5:
                    
                    if validacao(cod,'turmas'): # Validação.
                        print('\nCódigo de turma não encontrado.\n'
                            'Tente novamente.')
                    else:
                        cod_estudante = codigo_excecoes('estudante')
                        if validacao(cod_estudante,'estudantes'): # Validação.
                            print('\nCódigo de estudante não encontrado.\n'
                                'Tente novamente.')
                        else:
                            dados = {'código':cod,'codestudante':cod_estudante}
                            tabela.append(dados)
                            escrever_json(tabela,nome)
                            print('\nCadastro concluído com sucesso')
            
        # Após concluir a inclusão de um cadastro, é apresentado a pergunta:
        if input('Deseja realizar outro cadastro? (s/n) ').strip().lower() == 'n': # Se digitar qualquer coisa além de 'n', o programa continua na inclusão.
            break

# Função que verifica e faz a validação do código fornecido na inclusão de turmas e matrículas.
def validacao(codigo,tabela): # Recebe como parâmetro o código que é para verificar e a tabela a qual ele pertence.
    tabela_validacao = ler_json(tabela) # Tabela a qual vamos tentar validar aquele código. (tabela a qual ele deve pertencer).
    if len(tabela_validacao) == 0: # Se estiver vazia já retorna True.
        return True
    for cadastros in tabela_validacao:
        if codigo in cadastros.values(): # Se encontrar o código nos valores das chaves daquela tabela, retorna False.
            return False
    return True # Se não, retorna True.

# Função que checa se já não há aquele código ou cpf na tabela onde ele iria ser incluído.
def checagem_duplicata(cod,tabela,nome): # Recebe como parâmetro: o código a ser verificado, a tabela a qual ele estava a ser incluído e o nome do menu de onde o usuário veio.
    verif = False # verif vai ser a váriavel que guarda o valor da verificação, se for True, significa que aquele código já está cadastrado em outro registro.
    if nome == 'professores' or nome == 'estudantes': # Caso seja o menu dos professores ou estudantes:
        # O for vai percorrer a tabele procurando se aquele código ou cpf está presente em algum cadastro:
        for cadastro in tabela:
            if cod == cadastro['código'] or cod == cadastro['cpf']:
                verif = True
    else: # Caso seja qualquer outro:
        # O for vai percorrer a tabele procurando se aquele código está presente em algum cadastro:
        for cadastro in tabela:
            if cod == cadastro['código']:
                verif = True
    # E no fim, vai retornar o verif.
    return verif

# Função que realiza a listagem dos cadastros de cada tabela.
def listagem(menu): # menu = menu de onde o usuário veio.
    nome = nomes(menu) # nome vai receber o nome do menu
    tabela = ler_json(nome) # tabela vai receber o arquivo json do menu específico.
    if checagem_itens(nome): # Chama a função checagem_itens, para verificar se tem cadastros dentro da tabela.
        if nome in ['estudantes','professores','turmas']: # Como esses 3 menus possuem 3 caracteristicas, coloquei eles no mesmo bloco de código:
            # Fiz uma condicional pra atribuir o valor certo da chave.
            if nome == 'turmas': # Se for o menu das turmas, vão ser esses indices e chaves:
                indice2 = ['CÓDIGO DO PROFESSOR',"codprof"]
                indice3 = ['CÓDIGO DA DISCIPLINA',"coddisc"]
            else: # Se for o menu dos professores ou estudantes, vão ser esses indices e chaves:
                indice2 = 'NOME',"nome"
                indice3 = 'CPF',"cpf"
            # Formatei para que ficasse em um formato de tabela:
            linhas = '-'*60
            print(f'\n{nome.upper()} - LISTAGEM\n') # Identificando
            print(linhas)
            print(f'|{"CÓDIGO":^12}|{indice2[0]:^21}|{indice3[0]:^23}|') # Cabeçalho contendo a identificação, (usando os indices) dos itens que terá na tabela.
            print(linhas)
            # O for vai percorrer toda a tabela e imprimir os dados:
            for cadastro in tabela:
                # Usei os indices para que funcionasse bem para os 3 menus.
                print(f'|{cadastro["código"]:^12}|{cadastro[indice2[1]]:^21}|{cadastro[indice3[1]]:^23}|')
                print(linhas)
        # Para os cadastros das disciplinas e matriculas eu utilizei da mesma lógica:
        elif nome in ['disciplinas','matriculas']:
            if nome == 'disciplinas':
                indice1 = 'CÓDIGO DA DISCIPLINA'
                indice2 = ['NOME DA DISCIPLINA','nome']
            elif nome == 'matriculas':
                indice1 = 'CÓDIGO DA TURMA'
                indice2 = ['CÓDIGO DO ESTUDANTE','codestudante']
            linhas = '-'*46
            print(f'\n{nome.upper()} - LISTAGEM\n')
            print(linhas)
            print(f'|{indice1:^22}|{indice2[0]:^21}|')
            print(linhas)
            for cadastro in tabela:
                print(f'|{cadastro["código"]:^22}|{cadastro[indice2[1]]:^21}|')
                print(linhas)
    # Caso a função checagem_itens retorne False:
    else:
        print(f'Não há nenhum cadastro de {nome}.')

# Função de exclusão de cadastros.
def exclusao(menu):
    excluindo = True # excluindo começa com True para que o loop aconteça:
    while excluindo == True:
        nome = nomes(menu)
        tabela = ler_json(nome)
        if checagem_itens(nome): # Sempre começa verificando se tem cadastros dentro da tabela daquele menu.
                # excluido vai ser uma forma de confirmação se um cadastro foi excluido ou não.
                excluido = False # Começa com False.
                print(f'\n{nome} - EXCLUSÃO')
                # Loop para evitar erro de conversão:
                while True:
                    try:
                        cod = int(input('Digite o código a ser excluído: '))
                        break
                    except:
                        print('O valor precisa ser um inteiro, tente novamente.\n')
                # o for percorre a lista procurando o código que o usuário deseja excluir:
                for cadastros in tabela:
                    if cod == cadastros['código']: # Caso encontre, o remove:
                        tabela.remove(cadastros)
                        escrever_json(tabela,nome) # E salva as alterações na respectiva tabela.
                        excluido = True # excluido recebe True pra confirmar a exclusão do cadastro.
                if excluido:
                    print('Cadastro excluido com sucesso.')
                # Se excluido não receber True (o programa não encontrar o código para exclui lo):
                else:
                    print('Não foi possível encontrar um cadastro com esse código.')
                # Caso o usuário queira excluir outro cadastro ele não precisa voltar ao menu para selecionar essa opção novamente:
                if str(input('Deseja excluir outro cadastro? (s/n): ')).strip().lower() == 'n':
                    excluindo = False
        # Se não tiver nenhum cadastro na tabela, aparece uma mensagem e excluindo recebe False, para que o loop encerre.
        else:
            print(f'Não há nenhum cadastro de {nome}.')
            excluindo = False

# Verifica se o código escolhido para atualizar realmente pertence a um cadastro daquela tabela.
# cod = código do cadastro que o usuário quer atualizar, nome = menu de onde o usuário veio.
def verificacao(cod,nome): 
    tabela = ler_json(nome)
    for cadastros in tabela:
        # Caso tenha o código em algum cadastro da tabela, retorna True.
        if cod == cadastros['código']: 
            return True
    # Caso não tenha, retorna False.
    return False

# Realiza a pergunta do código do cadastro que o usuário deseja atualizar e garante que ele seja um inteiro.
def pergunta_atualizacao():
    while True:
            try:
                cod_atualizar = int(input('Digite o código a ser atualizado: '))
                break
            except:
                print('O valor precisa ser um inteiro. Tente novamente')
    return cod_atualizar

# Função que realiza a atualização de cadastros:
def atualizacao(menu):
    nome = nomes(menu)
    if checagem_itens(nome): # Se tiver cadastros dentro da tabela do menu:
        print(f'\n{nome.upper()} - ATUALIZAÇÃO') # Identificação.
        tabela = ler_json(nome)
        while True:
            # cod_atualizar vai receber o código retornado da função pergunta_atualizacao
            cod_atualizar = pergunta_atualizacao()
            if verificacao(cod_atualizar,nome): # Chama a função verificacao para verificar se aquele código realmente pertence a algum cadastro da tabela, caso sim:
                print('\nDIGITE OS NOVOS DADOS:')
                cod = codigo_excecoes(nome) # Novo código do cadastro
                # atualização de estudantes ou professores
                if menu in [1,2]:
                    # Chama a função checagem_profunda, que verifica se o novo código já não pertence a algum outro cadastro que não seja o mesmo.
                    if checagem_profunda(cod,cod_atualizar,nome,"código"): # Caso retorne True (que pertence):
                        print('Já tem um cadastro com esse código, podendo ser estudante ou professor. Verifique e tente novamente.')
                    else: # Caso retorne False (que não pertence):
                        nomecadastro = str(input(f'Digite o nome do {nome}: ')).strip().title() # Novo nome do cadastro
                        # Loop que verifica se o cpf digitado é válido (se tem 11 caracteres):
                        while True:
                            cpf = str(input(f'Digite o CPF do {nome}: '))
                            if len(cpf) == 11:
                                break # Só sai do loop após o usuário digitar um cpf válido.
                            elif len(cpf) < 11:
                                print('CPF inválido, tente novamente, dessa vez utilizando um com 11 caracteres.')
                        # Chama a função checagem_profunda, que verifica se o novo cpf já não pertence a algum outro cadastro que não seja o mesmo.
                        if checagem_profunda(cpf,cod_atualizar,nome,"cpf"): # Caso retorne True:
                            print('Já tem um cadastro com esse cpf, podendo ser estudante ou professor. Verifique e tente novamente.')
                        else: # Caso retorne False:
                            # Armazena os dados passados em um dicíonario.
                            dados = {'código':cod,'nome':nomecadastro,'cpf':cpf}
                            # O for percorre a lista procurando o cadastro que possua o código do cadastro que o usuário quer alterar:
                            for cadastros in tabela:
                                if cod_atualizar == cadastros['código']: # Quando encontrar:
                                    cadastros.update(dados) # Atualiza o cadastro com os novos dados.
                                    escrever_json(tabela,nome) # Grava as alterações feitas na tabela.
                                    print('Cadastro atualizado com sucesso.') # Imprime uma mensagem de sucesso.
                # Caso seja o menu 3, 4 ou 5:
                elif menu in [3,4,5]:
                    #atualização de disciplinas
                    if menu == 3:
                        # Mesma lógica...(checagem para evitar código duplicados e manter a integridade dos dados...)
                        if checagem_profunda(cod,cod_atualizar,nome,"código"):
                            print('Já tem um cadastro com esse código. Verifique e tente novamente.')
                        else:
                            nomecadastro = str(input(f'Digite o novo nome da {nome}: ')).strip().title() # Novo nome da disciplina.
                            # Mesma lógica...
                            dados = {'código':cod,'nome':nomecadastro}
                            for cadastros in tabela:
                                if cod_atualizar == cadastros['código']:
                                    cadastros.update(dados)
                                    escrever_json(tabela,nome)
                                    print('Cadastro atualizado com sucesso.')
                    # atualização de turmas       
                    elif menu == 4:
                        if checagem_profunda(cod,cod_atualizar,nome,"código"):
                            print('Já tem um cadastro com esse código. Verifique e tente novamente.')
                        else:
                            cod_professor = codigo_excecoes('professor')
                            if validacao(cod_professor,"professores"): # Chama a função validacao para verificar se o novo código é válido e se tem algum professor com ele.
                                print('\nCódigo de professor não encontrado. Tente novamente.')
                            else:
                                cod_disciplina = codigo_excecoes('disciplina')
                                if validacao(cod_disciplina,'disciplinas'): # Chama a função validacao para verificar se o novo código é válido e se tem alguma disciplina com ele.
                                    print('\nCódigo de disciplina não encontrado.\n'
                                        'Tente novamente.')
                                else:
                                    dados = {'código':cod,'codprof':cod_professor,'coddisc':cod_disciplina}
                                    for cadastros in tabela:
                                        if cod_atualizar == cadastros['código']:
                                            cadastros.update(dados)
                                            escrever_json(tabela,nome)
                                            print('Cadastro atualizado com sucesso.')
#----------------------------------------------------(mesma lógica de atualização)------------------------------------------------------#                                              
                # atualização de matrículas
                    elif menu == 5:
                        if checagem_profunda(cod,cod_atualizar,nome,"código"):
                            print('Já tem um cadastro com esse código. Verifique e tente novamente.')
                        else:
                            if validacao(cod,'turmas'):
                                print('\nCódigo de turma não encontrado.\n'
                                    'Tente novamente.')
                            else:
                                cod_estudante = codigo_excecoes('estudante')
                                if validacao(cod_estudante,'estudantes'):
                                    print('\nCódigo de estudante não encontrado.\n'
                                        'Tente novamente.')
                                else:
                                    dados = {'código':cod,'codestudante':cod_estudante}
                                    for cadastros in tabela:
                                        if cod_atualizar == cadastros['código']:
                                            cadastros.update(dados)
                                            escrever_json(tabela,nome)
                                            print('Cadastro atualizado com sucesso.')
            # Caso o código que o usuário digitou não pertencer a nenhum cadastro da tabela:
            else:
                print('Não foi encontrado um cadastro com esse código')
            if input('Deseja atualizar outro cadastro? (s/n) ').strip().lower() == 'n':
                break
    # Caso não tenha cadastros na tabela.        
    else:
        print(f'Não há nenhum cadastro de {nome}')

# Essa função é extremamente importante pra integridade dos dados. Ela é chamada na função atualizacao.
# Ela verifica se aquele código novo que o usúario escolheu para a atualização já não está cadastrado em outro cadastro.
# Também faz a mesma verificação com o cpf do estudante ou professor.
# dado = é o dado que a função vai verificar se já tem em algum outro cadastro ou não, no caso de estudantes e professores 
# pode ser tanto o cpf quanto o código, nos outros casos, apenas o código.
# codigoatualizacao = é o código do cadastro que está sendo atualizado
# nome = é o nome do menu onde o úsuario se encontra
# chave = é a chave do dicíonario para ser usada na estrutura for, se estivermos verificando um código, a chave será 'código', se for um cpf a chave será 'cpf'.     
def checagem_profunda(dado,codigoatualizacao,nome,chave):
    tabela = ler_json(nome) # Abre a tabela específica daquele cadastro que está sendo atualizado.
    for cadastros in tabela: # Percorre a tabela verificando os cadastros:
        # Se tiver um cadastro com aquele mesmo dado e o código desse cadastro é diferente do código do cadastro que estamos atualizando:
        if cadastros[chave] == dado and cadastros['código'] != codigoatualizacao:  
# Aqui é importante ter essa verificação se o cadastro é diferente do que estamos atualizando porque quero permitir que o úsuario atualize um cadastro repetindo as mesmas informações.
            return True # Retorna True
    return False # Caso não encontre, retorna False

# Função que verifica se há cadastros dentro da tabela referenciada pelo parâmetro nome.
def checagem_itens(nome):
    tabela = ler_json(nome) # Abre a tabela conforme o nome passado.
    if tabela != []: # Se a tabela estiver diferente de vazia:
        return True
    elif tabela == []: # Se estiver vazia:
        return False
    
# Essa função realiza o tratamento de exceção do input da pergunta do código. Ela evita que o programa dê erro tentando converter string em inteiro.
# Como essa pergunta é feita em vários momentos do programa eu achei mais prático fazer uma função destinada a ela.
def codigo_excecoes(nome): # O parâmetro nome é nada menos que a identifição do menu em que o úsuario se encontra. Caso ele queira incluir um aluno o nome será Estudantes e assim por diante.
    while True: # Loop infinito que só se encerra quando o usúario digita um inteiro.
        try:
            if nome == 'matriculas':
                nome = 'turma'
            else:
                cod = int(input(f'\nDigite o código de {nome}: ')) # Digite o código de estudantes ou professores ou disciplinas[...]
                break # Se for inteiro, encerra o loop.
        except: # Se não, imprime a mensagem:
            print('O valor precisa ser um inteiro. Tente novamente.')
    return cod # Validando o código como um inteiro, ele retorna o código.

# Função que gera todos os json equivalente aos menus no primeiro início do programa para evitar erros. Ela trabalha juntamente com o except da função ler_json.
def primeiro_inicio():
    tabelas = ['estudantes','professores','disciplinas','turmas','matriculas'] # nomes dos arquivos json que serão criados
    for tabela in tabelas:
        # Aqui eu fui atribuindo as tabelas criada a uma única varíavel chamada tabela_de_dados, ela só será usada para a chamada da criação das tabelas.
        tabela_de_dados = ler_json(tabela) # Ta usando como parâmetro os nomes contidos na váriavel tabelas para nomear os arquivos json a serem criados.

# Chamei a função do primeiro início.
primeiro_inicio()
# E a função do menu inicial.
menu_inicial()