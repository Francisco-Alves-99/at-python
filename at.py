def cadastrar_produto(produto):
    """
    Cadastra um novo produto na lista de produtos.

    A função recebe uma string contendo os atributos de um produto separados por ponto e vírgula (';'),
    e a converte em um dicionário, onde cada chave corresponde a um atributo do produto. O dicionário é
    então adicionado à lista global de produtos.

    Parâmetros:
    produto (str): Uma string contendo os atributos do produto, separados por ponto e vírgula. 
                   A ordem dos atributos deve corresponder à ordem definida na lista `chaves`.

    Exemplo:
    Se `chaves` for ['nome', 'preco', 'quantidade'], e o argumento `produto` for 'Produto A;25.99;10',
    o dicionário {'nome': 'Produto A', 'preco': '25.99', 'quantidade': '10'} será adicionado à lista
    `lista_produtos`.
    """
    atributos = produto.split(';') # Separa os atributos através do separador informado

    produto_dict = {chaves[i]: atributos[i] for i in range(len(chaves))} # Cria o dicionário com o produto

    lista_produtos.append(produto_dict) # Adiciona o produto na lista

def usuario_cadastra_produto():
    """
    Solicita ao usuário os dados necessários para cadastrar um novo produto e os envia para a função
    `cadastrar_produto` para inclusão na lista de produtos.

    A função realiza as seguintes etapas:
    1. Solicita a descrição do produto.
    2. Gera um código único para o produto utilizando a função `gerar_codigo_unico`.
    3. Solicita a quantidade, custo do item e preço de venda do produto.
    4. Organiza os dados em uma string, com cada valor separado por ponto e vírgula (';').
    5. Chama a função `cadastrar_produto` para registrar o produto na lista de produtos.

    A função não retorna nenhum valor, mas adiciona o novo produto à lista global de produtos.

    Exemplo de fluxo de entrada:
    - "Digite a descrição do produto: Produto X"
    - "Digite a quantidade: 100"
    - "Digite o custo do item: 50.00"
    - "Digite o preço de venda: 75.00"

    O produto será cadastrado com a descrição, código único gerado, quantidade, custo e preço de venda informados.
    """
    valores = [] # lista que irá acomodar os valores digitados pelo usuário
    descricao = input("Digite a descrição do produto: ")
    valores.append(descricao)
    novo_codigo = gerar_codigo_unico()
    valores.append(str(novo_codigo))
    quantidade = input("Digite a quantidade: ")
    valores.append(quantidade)
    custo_item = input("Digite o custo do item: ")
    valores.append(custo_item)
    preco_venda = input("Digite o preço de venda: ")
    valores.append(preco_venda)
    # os inputs acima guardam os valores em variáveis
    produto = ';'.join(valores) # adiciona um separador nos valores
    cadastrar_produto(produto) # chama a funcao que cadastra os produtos

def gerar_codigo_unico():
    """
    Gera um novo código único para um produto, baseado no maior código já cadastrado na lista de produtos.

    A função procura o maior valor de código presente na lista global `lista_produtos` e gera um novo código
    incrementando o valor do maior código encontrado em 1. Esse novo código é retornado para ser utilizado no
    cadastro de um novo produto.

    A função assume que a lista `lista_produtos` contém produtos cadastrados com um campo 'codigo'.

    Retorna:
    int: O novo código único gerado para o próximo produto a ser cadastrado.

    Exemplo de uso:
    Se os códigos cadastrados forem [1, 2, 3], a função retornará 4 como o próximo código.
    """
    maior_codigo = max(produto['codigo'] for produto in lista_produtos) # procura qual é o maior código cadastrado na lista de produtos
    novo_codigo = int(maior_codigo) + 1 # soma + 1 no maior código para gerar um novo único
    return novo_codigo # retorna o código

def listar_produtos(lista):
    """
    Exibe no terminal a lista de produtos, mostrando suas chaves e valores.

    A função percorre a lista fornecida e, para cada produto (representado como um dicionário), imprime
    suas chaves e respectivos valores no formato "chave: valor". Após exibir os dados de cada produto,
    é impressa uma linha separadora para melhorar a leitura.

    Parâmetros:
    lista (list): Uma lista de dicionários, onde cada dicionário representa um produto e contém
                  pares de chave-valor correspondentes às propriedades do produto.

    Exemplo de uso:
    Se a lista contiver:
    [
        {'codigo': '1', 'descricao': 'Produto A', 'quantidade': '10', 'preco': '15.99'},
        {'codigo': '2', 'descricao': 'Produto B', 'quantidade': '20', 'preco': '25.99'}
    ]
    A função irá exibir:
    Produto:
    codigo: 1
    descricao: Produto A
    quantidade: 10
    preco: 15.99
    --------------------
    Produto:
    codigo: 2
    descricao: Produto B
    quantidade: 20
    preco: 25.99
    --------------------
    """
    for produto in lista:
        print("Produto:")
        for chave, valor in produto.items():
            print(f"{chave}: {valor}") # para cada produto na lista é printado no terminal com sua chave e valor
        print("-" * 20)

def ordena_produtos():
    """
    Ordena a lista de produtos com base na quantidade, de acordo com a escolha do usuário.

    A função solicita ao usuário que escolha entre ordenar a lista de produtos por quantidade de forma crescente
    ou decrescente. Em seguida, a lista é ordenada utilizando a função `sorted()`, com a chave sendo a quantidade
    de cada produto. Após a ordenação, a função `listar_produtos` é chamada para exibir a lista ordenada no terminal.

    O usuário deve digitar:
    - 1 para ordenar de forma crescente (do menor para o maior valor de quantidade).
    - 2 para ordenar de forma decrescente (do maior para o menor valor de quantidade).

    Exemplo de uso:
    Se a lista de produtos contiver:
    [
        {'codigo': '1', 'descricao': 'Produto A', 'quantidade': '5'},
        {'codigo': '2', 'descricao': 'Produto B', 'quantidade': '10'},
        {'codigo': '3', 'descricao': 'Produto C', 'quantidade': '2'}
    ]
    
    E o usuário escolher a opção 1 (crescente), a saída será:
    Produto:
    codigo: 3
    descricao: Produto C
    quantidade: 2
    --------------------
    Produto:
    codigo: 1
    descricao: Produto A
    quantidade: 5
    --------------------
    Produto:
    codigo: 2
    descricao: Produto B
    quantidade: 10
    --------------------
    """
    escolha = int(input("Digite 1 para ordenar por ordem crescente ou 2 para ordenar por ordem decrescente ")) # pede para o usuário escolher entre ordenar de forma crescente ou decrescente

    if escolha == 1:
        lista_ordem_crescente = sorted(lista_produtos, key=lambda x: int(x['quantidade'])) # ordena a lista de forma crescente
        listar_produtos(lista_ordem_crescente)
    elif escolha == 2:
        lista_ordem_decrescente = sorted(lista_produtos, key=lambda x: int(x['quantidade']), reverse=True) # ordena a lista  de forma decrescente
        listar_produtos(lista_ordem_decrescente)

def buscar_produtos(**kwargs):
    """
    Busca produtos na lista `lista_produtos` com base nos critérios fornecidos como parâmetros nomeados.

    A função permite realizar uma busca flexível pelos atributos dos produtos, como descrição e código.
    O usuário pode passar parâmetros nomeados para buscar produtos que atendam a determinados critérios.

    Parâmetros:
    - descricao (str, opcional): A descrição do produto a ser buscada. A busca é feita de forma insensível a maiúsculas/minúsculas.
    - codigo (str, opcional): O código do produto a ser buscado. O código é comparado de forma exata (sem distinção de maiúsculas/minúsculas).

    A função verifica se os parâmetros 'descricao' ou 'codigo' foram fornecidos, e filtra os produtos com base
    nesses valores. Produtos que atendem a qualquer critério de busca são adicionados à lista `resultados`.

    Retorna:
    - list: Uma lista de produtos (dicionários) que atendem aos critérios de busca. Se nenhum critério for fornecido
            ou se nenhum produto corresponder, a lista retornada será vazia.

    Exemplo de uso:
    - Busca por descrição: `buscar_produtos(descricao='Produto A')`
    - Busca por código: `buscar_produtos(codigo='1')`
    - Busca por descrição e código: `buscar_produtos(descricao='Produto', codigo='2')`

    Exemplo de saída (caso a lista contenha um produto com descrição "Produto A" e código "1"):
    [
        {'codigo': '1', 'descricao': 'Produto A', 'quantidade': '10', 'preco': '15.99'}
    ]
    """
    resultados = [] # lista para guardar os resultados

    for produto in lista_produtos:
        # Obtém os valores de 'descricao' e 'codigo' fornecidos como argumentos nomeados.
        descricao = kwargs.get('descricao', '').lower()
        codigo = kwargs.get('codigo', '').lower()

        # Verifica se 'descricao' foi fornecida e se corresponde à descrição do produto (ignorando maiúsculas/minúsculas)
        if descricao and descricao in produto['descricao'].lower():
            resultados.append(produto)
        # Verifica se 'codigo' foi fornecido e se corresponde exatamente ao código do produto    
        elif codigo and codigo == str(produto['codigo']):
            resultados.append(produto)

    return resultados

def entrada_usuario_busca():
    """
    Solicita ao usuário uma entrada (descrição ou código de produto) e realiza uma busca na lista de produtos.

    A função pede ao usuário que insira uma descrição ou código de produto. Dependendo da entrada, ela chama a 
    função `buscar_produtos` para buscar produtos com base na descrição (se a entrada for texto) ou no código 
    (se a entrada for numérica). Em seguida, exibe os produtos encontrados ou uma mensagem informando que o produto 
    não foi encontrado.

    Fluxo de operação:
    1. O usuário é solicitado a digitar um critério de busca (descrição ou código).
    2. A função verifica se a entrada é um número (indicando que o usuário forneceu um código).
    3. Realiza a busca através da função `buscar_produtos` com o critério apropriado.
    4. Se produtos forem encontrados, a função exibe os resultados usando `listar_produtos`.
    5. Caso contrário, exibe uma mensagem informando que o produto não existe.
    """

    # Solicita a entrada do usuário para busca (descrição ou código)
    entrada_usuario = input("Digite a descrição ou código do produto: ").strip()

    if entrada_usuario.isdigit():  # Verifica se a entrada é um número (código do produto)
        resultados = buscar_produtos(codigo=entrada_usuario) # Chama a função de busca passando o código como parâmetro
    else:
        # Caso contrário, assume-se que a entrada é uma descrição
        resultados = buscar_produtos(descricao=entrada_usuario)

    if resultados:
        print("\nProdutos encontrados:")
        listar_produtos(resultados)
    else:
        print("Produto não existente")

def remover_produto():
    """
    Solicita ao usuário o código de um produto e remove-o da lista de produtos.

    A função pede ao usuário que insira o código de um produto a ser removido. Em seguida, percorre a lista de produtos
    e verifica se o código informado corresponde a algum produto. Se o produto for encontrado, ele é removido da lista.
    Caso o produto não seja encontrado, uma mensagem de erro é exibida.

    Fluxo de operação:
    1. O usuário é solicitado a digitar o código do produto a ser removido.
    2. A função percorre a lista de produtos e compara o código informado com o código de cada produto.
    3. Se o código corresponder, o produto é removido da lista e uma mensagem de sucesso é exibida.
    4. Se o produto não for encontrado, uma mensagem informando que o produto não existe é exibida.
    """
    produto_escolhido = input("Digite o código do produto que deseja remover: ") # Solicita ao usuário o código do produto a ser removido
    for produto in lista_produtos:
        if produto_escolhido == produto['codigo']: # Verifica se o código existe na lista
            lista_produtos.remove(produto) # Remove o produto da lista
            print("Produto removido com sucesso!")
            return
    print('Produto não encontrado')

def exibir_produtos_esgotados():
    """
    Exibe os produtos que estão esgotados na lista de produtos.

    A função percorre a lista de produtos e verifica quais possuem quantidade igual a '0' (indicando que estão esgotados). 
    Os produtos esgotados são então armazenados em uma lista e exibidos utilizando a função `listar_produtos`.

    Fluxo de operação:
    1. A função percorre todos os produtos da lista `lista_produtos`.
    2. Para cada produto, verifica se o valor da quantidade é igual a '0' (indicando que o produto está esgotado).
    3. Adiciona os produtos esgotados à lista `produtos_esgotados`.
    4. Exibe os produtos esgotados utilizando a função `listar_produtos`.

    Exemplo de uso:
    Se a lista de produtos contiver:
    [
        {'codigo': '1', 'descricao': 'Produto A', 'quantidade': '0'},
        {'codigo': '2', 'descricao': 'Produto B', 'quantidade': '10'}
    ]
    
    A função exibirá:
    Produto:
    codigo: 1
    descricao: Produto A
    quantidade: 0
    --------------------
    """
    produtos_esgotados = [] # cria uma lista vazia para guardar os produtos esgotados
    for produto in lista_produtos:
        if produto['quantidade'] == '0': # verifica se existe produtos com a quantidade igual a 0
            produtos_esgotados.append(produto) # se tiver, guarda na lista para ser exibido posteriormente
    listar_produtos(produtos_esgotados) # chama a funcao de listar produtos passando aqueles que estão esgotados

def filtrar_quantidade(qntd=7):
    """
    Filtra e exibe os produtos cuja quantidade é menor que o valor especificado.

    A função percorre a lista de produtos e seleciona os produtos cuja quantidade (convertida para inteiro)
    é menor que o valor fornecido no parâmetro `qntd`. A lista filtrada é então exibida utilizando a função `listar_produtos`.

    Parâmetros:
    qntd (int, opcional): O valor de referência para filtrar os produtos. Somente produtos com quantidade menor que
                          esse valor serão exibidos. O valor padrão é 7.

    Fluxo de operação:
    1. A função percorre a lista de produtos e compara a quantidade de cada produto com o valor de `qntd`.
    2. Produtos cuja quantidade é inferior a `qntd` são adicionados à lista `produtos_filtrados`.
    3. A lista de produtos filtrados é exibida utilizando a função `listar_produtos`.

    Exemplo de uso:
    - Se `lista_produtos` contiver os produtos:
    [
        {'codigo': '1', 'descricao': 'Produto A', 'quantidade': '5'},
        {'codigo': '2', 'descricao': 'Produto B', 'quantidade': '10'},
        {'codigo': '3', 'descricao': 'Produto C', 'quantidade': '3'}
    ]
    - E a função for chamada como `filtrar_quantidade(7)`, ela exibirá:
    Produto:
    codigo: 1
    descricao: Produto A
    quantidade: 5
    --------------------
    Produto:
    codigo: 3
    descricao: Produto C
    quantidade: 3
    --------------------
    """
    produtos_filtrados = [produto for produto in lista_produtos if int(produto['quantidade']) < qntd] # Filtra os produtos cuja quantidade é menor que o valor fornecido (padrão é 7)
    listar_produtos(produtos_filtrados) # Chama a funcao de listar produtos passando aqueles que cumprem o requisito

def atualiza_quantidade():
    produto_escolhido = input("Digite o código do produto que deseja atualizar: ") # solicita ao usuário que digite o código do produto escolhido
    for produto in lista_produtos:
        if produto_escolhido == produto['codigo']: # verifica se o produto existe na lista
            nova_quantidade = input("Digite a quantidade atualizada: ") # solicita a quantidade para atualizar
            if int(nova_quantidade) < 0: # se for um número negativo, ele encerra a operaçao
                print("Quantidade não permitida!")
                return
            else:    
                produto['quantidade'] = nova_quantidade # se for um número válido, atualiza a quantidade na lista
                print("Quantidade atualizada com sucesso!")
                return
    print('Produto não encontrado')

def atualiza_preco():
    produto_escolhido = input("Digite o código do produto que deseja atualizar: ") # solicita ao usuário que digite o código do produto escolhido
    for produto in lista_produtos:
        if produto_escolhido == produto['codigo']: # verifica se o produto existe na lista
            novo_preco = input("Digite o preço atualizado: ") # solicita o preço para atualizar
            if float(novo_preco) < float(produto['custo_item']): # se for menor que o custo do item, a operaçao encerra
                print("Novo preço é menor que o custo do item!")
                return
            else:    
                produto['preco_venda'] = novo_preco # se for válido, ele atualiza o preço na lista
                print("Preço atualizado com sucesso!")
                return
    print('Produto não encontrado') 

def valor_total():
    valor_total = 0 # cria a variável para comportar o valor total

    for produto in lista_produtos:
        valor_total += int(produto['quantidade']) * float(produto['preco_venda']) # multiplica a quantidade pelo preço e soma na variável
    print(f"O valor total do estoque é: R$ {valor_total:.2f}")   

def lucro_presumido():
    lucro_presumido = 0 # cria a variável para comportar o lucro presumido

    for produto in lista_produtos:
        diferenca = float(produto['preco_venda']) - float(produto['custo_item']) # calcula a diferença do custo do item e o seu preço
        lucro_presumido += diferenca * int(produto['quantidade']) # multiplica a diferença pela quantidade e soma no lucro presumido

    print(f"O lucro total do estoque é R$ {lucro_presumido:.2f}")

def relatorio_geral():
    # Cabeçalho do relatório
    print(f"{'Descrição'.ljust(30)}{'Código'.rjust(10)}{'Quantidade'.rjust(15)}{'Custo'.rjust(10)}{'Preço Venda'.rjust(15)}{'Custo Total'.rjust(15)}{'Faturamento Total'.rjust(20)}")
    print("="*120)  # Linha de separação
    
    custo_total_estoque = 0.0
    faturamento_total_estoque = 0.0

    # Exibe cada produto do estoque
    for produto in lista_produtos:
        descricao = produto['descricao'].ljust(30)
        codigo = produto['codigo'].rjust(10)
        quantidade = produto['quantidade'].rjust(15)
        custo_item = produto['custo_item'].rjust(10)
        preco_venda = produto['preco_venda'].rjust(15)
        
        # Calcula o custo total e faturamento total para o item
        custo_total = float(produto['quantidade']) * float(produto['custo_item'])
        faturamento_total = float(produto['quantidade']) * float(produto['preco_venda'])
        
        # Atualiza os totais do estoque
        custo_total_estoque += custo_total
        faturamento_total_estoque += faturamento_total
        
        # Formata os valores de custo total e faturamento total
        custo_total_formatado = f"{custo_total:.2f}".rjust(15)
        faturamento_total_formatado = f"{faturamento_total:.2f}".rjust(20)

        # Imprime os dados formatados
        print(f"{descricao}{codigo}{quantidade}{custo_item}{preco_venda}{custo_total_formatado}{faturamento_total_formatado}")

    # Exibe o total geral do estoque
    print("="*120)
    print(f"{'TOTAL GERAL'.ljust(30)}{'':>10}{'':>15}{'':>10}{'':>15}{f'{custo_total_estoque:.2f}'.rjust(15)}{f'{faturamento_total_estoque:.2f}'.rjust(20)}")     

def menu_interativo():
    # loop de repetiçao para exibir o menu constantemente
    while True:
        print("-" * 20)
        print("M E N U")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Ordenar produtos por quantidade")
        print("4. Buscar produto")
        print("5. Remover produto")
        print("6. Consultar produtos esgotados")
        print("7. Filtrar produtos com baixa quantidade")
        print("8. Atualizar quantidade")
        print("9. Atualizar preço")
        print("10. Calcular valor total do estoque")
        print("11. Calcular lucro presumido")
        print("12. Relatório geral do estoque")
        print("13. Sair")
        print("-" * 20)
        escolha = int(input("Digite o número da opção desejada: ")) # guarda a opcao digitada pelo usuário


        # um switch case para chamar as funcoes de acordo com a opcao do usuário
        match(escolha):
            case 1:
                usuario_cadastra_produto()
            case 2:
                listar_produtos(lista_produtos)
            case 3:
                ordena_produtos()
            case 4:
                entrada_usuario_busca()
            case 5:
                remover_produto()
            case 6:
                exibir_produtos_esgotados()
            case 7:
                escolha_filtro = int(input("Digite 1 para especificar a quantidade ou 2 para usar a padrão do sistema: ")) # dá a opcao do usuário especificar ou nao
                if escolha_filtro == 1:
                    filtro_usuario = int(input("Digite a quantidade para ser filtrado: ")) # guarda a quantidade digitada pelo usuário
                    filtrar_quantidade(filtro_usuario)
                else:
                    filtrar_quantidade()
            case 8:
                atualiza_quantidade()
            case 9:
                atualiza_preco()
            case 10:
                valor_total()
            case 11:
                lucro_presumido()
            case 12:
                relatorio_geral()
            case 13:
                break    

        # permite que o usuário saia ou volte ao menu após a operacao ser encerrada        
        escolha_2 = int(input("Digite 1 para voltar ao menu ou 2 para sair: "))
        if escolha_2 == 2:
            break                                                            
     

# estoque inicial com os produtos
estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"
produtos = estoque_inicial.split('#') # separando pelo demarcador

lista_produtos = [] # lista que irá comportar os produtos

chaves = ['descricao', 'codigo', 'quantidade', 'custo_item', 'preco_venda'] # as chaves que os produtos terão

# cadastra os produtos na lista
for produto in produtos:
    cadastrar_produto(produto)

menu_interativo()    


          
