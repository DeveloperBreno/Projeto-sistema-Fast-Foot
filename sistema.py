# chamar pedido
import time

# ganhar desconto
def ganhardesconto(d):
    limpar()
    nomeupper = ''
    escrever('GANHAR DESCONTO [1]SIM [2]NÃO')
    desconto = int(input(''))
    cpflimpo = ' '
    if desconto == 2:
        return novopedido(nomeupper, cpflimpo)

    if desconto == 1:
        limpar()
        nomec = ''
        while len(nomec) < 3:
            escrever('NOME: ')
            nomec = input('')

        # upper
        nomeupper = nomec.upper()

        cpflimpo = ""
        while (len(cpflimpo) < 10) or len(cpflimpo) > 11:
            escrever('CPF:')
            cpflimpo = str(input(''))

            if len(cpflimpo) == 10:
                cpflimpo = "0" + cpflimpo

        ddd = ""
        while len(ddd) != 2:
            escrever('DDD:')
            ddd = str(input(''))

        tel = ""
        while len(tel) != 9:
            escrever('TELEFONE:')
            tel = str(input(''))

        # importar data
        from datetime import datetime
        now = datetime.now()

        # conctenar minutus horas dia mes ano
        data = (str(now.minute) + ":" + str(now.hour) + ";" + str(now.day) + "/" + str(now.month) + "/" + str(now.year))

        # linha para salvar
        linhacliente = (cpflimpo + ";" + nomeupper + ";" + ddd + ";" + tel + ";" + data + "\n")

        # abrir ou criar arquivo
        arquivo = open('cliente.csv', 'a',encoding="utf8", newline="")

        # escrever linha
        arquivo.write("%s" % linhacliente)

        # fechar
        arquivo.close()

        novopedido(nomeupper,cpflimpo)

    if desconto == 2:
        limpar()
        return novopedido(1)




def desconto_para_clientes_cadastrados(cpflimpo, total):
    if len(cpflimpo) >= 10:
        descontototal = total / 20# cinco % de desconto
        return descontototal
    else:
        return 0
















#pedido na tela
def chamarpedido(d):
    limpar()
    escrever('digite O PEDIDO: ')
    chamarpedido = int(input(''))
    limpar()
    escrever(str(chamarpedido))
    escrever(str(chamarpedido) + ' CONCLUIDO [1] CANCELAR [0]')
    opchamar = 1
    opchamar = str(input(''))
    if opchamar == '0':
        return menu()

    return pedidotela(str(chamarpedido))

# chamar pedido com musica
def pedidotela(texto):
    limpar()

    import pygame
    pygame.init()
    limpar()
    pygame.mixer.music.load('ex01.mp3')
    limpar()
    pygame.mixer.music.play()
    # pygame.event.wait()
    limpar()
    tamanhotexto = len(texto) + 20
    print('#' * tamanhotexto)
    print(" " * 10, texto)
    print('#' * tamanhotexto)
    import time
    time.sleep(5)

# limpar tela
def limpar():
    return print("\n" * 100)

# novo pedido
def novopedido(nome,cpflimpo):
    limpar()

    # mais um comvalor 1 para fazer o primeiro pedido
    maisum = 1

    total = 0

    if len(nome) < 1:
        nomeok = 0
        while nomeok == 0:
            escrever("NOME DO CLIENTE: ")
            nomeup = input("")
            nome = nomeup.upper()
            limpar()
            escrever(nome)
            escrever('CONTINUAR     [1]')
            escrever('ALTERAR NOME? [0]')
            opnome = int(input(''))
            limpar()
            if opnome == 1:
                nomeok = 1



    dic={}
    lista=list()
    # mais um com o valor 1 para iniciar
    maisum = 1
    while maisum == 1:

        if len(str(lista)) > 2:

            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('JÁ ADICIONADO ')

            for add in lista:
                minhalinha = ''
                add.split(';')
                for um in add:
                    minhalinha = minhalinha+str(um)



                remover =', )\', ( '
                for i in range(0, len(remover)):
                    minhalinha = minhalinha.replace(remover[i], '')

                minhalinha = minhalinha.replace('|||', '')
                minhalinha = minhalinha.replace('||', '')
                minhalinha = minhalinha.replace('|', ' | ')

                print(minhalinha)

            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


        # ecolher sabor
        SABOR = addproduto(1)



        #escrever("SABORES:  \n  [1] CHOCOLATE \n  [2] MISTO \n  [3] CREME\n  [4] triplo chocolate Kopenhagen\n  [5] Kit Kat")

        # quantidade de sorvetes reverente ao sabor
        QTDO = 1
        escrever("QUANTIDADE: ")
        QTDO = (int(input("")))
        








        # cobertura extra só por categoria/grupo de produtos
        #######################################################

        # cobertura extra
        #escrever('COBERTURA EXTRA [1] SIM [2] NÃO')
        #coberturaextra=int(input(''))
        #if coberturaextra == 1:
        #    total = total + 2 # mais 2 reais de cobertura extra
        #    #abrirfoto('e')
        #    extra = ' COM COBERTURA EXTRA'

        #else:
        #    extra = 'SEM COBERTURA EXTRA'
        extra = ''


        # cobertura extra só por categoria/grupo de produtos
        #######################################################






        # preço total do pedido
        descontodef = calcularprecototal(QTDO, SABOR)
        total = total + descontodef
        linhadoproduto = str(SABOR)
        valorli = linhadoproduto.split('|')
        valorreal = float(valorli[1])
        valorreal = QTDO * valorreal
        total = total + valorreal










        # lista de sabor e quantidade
        um = str(QTDO)
        lista.append("|| {} | {} | {} ||".format(str(um), str(SABOR), str(extra)))




        # limpar tela
        limpar()



        # mostrar na tela os ja add
        if len(str(lista)) > 2:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('JÁ ADICIONADO ')



            for add in lista:
                minhalinha = ''
                add.split(';')
                for um in add:
                    minhalinha = minhalinha+str(um)

                remover = ', )\', ( '
                for i in range(0, len(remover)):
                    minhalinha = minhalinha.replace(remover[i], '')

                minhalinha = minhalinha.replace('|||', '')
                minhalinha = minhalinha.replace('||', '')
                minhalinha = minhalinha.replace('|', ' | ')
                minhalinha = minhalinha.replace(' | ', '?')
                minhalinha = minhalinha.replace('|', '')
                minhalinha = minhalinha.replace('?', ' | ')
                print(minhalinha)
            #print('\n')
            #print('TOTAL: '+str(total))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')




        escrever("mais um   [1]")
        escrever("finalizar [2]")
        maisum = int(input(''))


        if maisum == 2:
            maisum = 0

        # limpar tela
        limpar()









    # importar data
    from datetime import datetime

    # agora
    now = datetime.now()

    # conctenar minutus horas dia mes ano
    horahora = str(now.hour)
    if len(horahora)<2:
        horahora ='0'+str(now.hour)

    minutominuto=str(now.minute)
    if len(minutominuto)<2:
        minutominuto ='0'+str(now.minute)


    data = (horahora + ":" + minutominuto + ";" + str(now.day) + "/" + str(now.month) + "/" + str(now.year))


    # mostrar o pedido completo para o usuario para confirmar pedido/venda

    m = int(now.minute)
    h = int(now.hour)
    d = int(now.day)
    me = int(now.month)
    an = int(now.year)
    numeropedidovariavel = str(numeropedido(m, h, d, me, an))
    escrever('NOME: ' + nome)
    listalinha = str(lista)
    listalinha=listalinha.replace(' ','')
    listalinha=listalinha.replace(']','')
    listalinha=listalinha.replace('[','')
    listalinha=listalinha.replace('\"','')
    listalinha=listalinha.replace('||','')
    listalinha=listalinha.replace('|','?')
    listalinha=listalinha.replace(',','')

    listalinha=listalinha.replace('(','')
    listalinha=listalinha.replace('\'','')
    listalinha = listalinha.replace(')', '\n')
    listalinha = listalinha.replace(' | ', '?')
    listalinha = listalinha.replace('|', '')
    listalinha = listalinha.replace('?', ' | ')
    




    subtotal = total
    descontodefcpf = desconto_para_clientes_cadastrados(cpflimpo, total)
    total = total-descontodefcpf





    print('PEDIDO')
    escrever(str(listalinha))
    escrever('SUBTOTAL:  R$ ' + str("%.2f" % subtotal))
    escrever('DESCONTO:  R$ ' + str("%.2f" % descontodefcpf))
    escrever('TOTAL:     R$ ' + str("%.2f" % total))



    escrever(str())



    # conferir se esta correto
    opfinal = '1'
    escrever("CONTINUAR [ENTER] CANCELAR [0]")
    opfinal = input("")

    if opfinal == "":
        opfinal = '1'
    if opfinal == '0':
        menu()

    # limpar tela
    limpar()


    # escrever na tela
    escrever('PEDIDO: '+numeropedidovariavel+' SALVO!')


    # espera
    time.sleep(1)



    # ferificar cpf
    if len(cpflimpo) < 3:
        cpflimpo = 'SEM CPF'

    pedidoitem = ''


    for item in lista:
        pedidoitem = pedidoitem + str(item)



    tsub=str(subtotal)
    tdesc=str(descontodefcpf)
    ttotal=str(total)





    # linha para salvar em arquivo
    linha = ("p"+numeropedidovariavel +';'+str(cpflimpo)+';'+ nome +';' + data + ';'+str(tsub)+ ';' +str(tdesc)+ ';' +str(ttotal) +  "\n")



    # abrir ou criar arquivo
    arquivo = open('pedidosimples.csv', 'a', newline="", encoding="utf8")

    # escrever linha
    arquivo.write("%s" % linha)

    # fechar
    arquivo.close()


    # chamar pdf
    gerarpdfdetalhado(nome, numeropedidovariavel, lista,tsub, tdesc,total, data)



    # string da lista
    listavariavel = str(lista)


    cpf = str(cpflimpo)


    
    # SUBSTITUIR UM SPAÇO | POR NUMERO DO PEDIDO
    # remover os caracteres da string
    remover = "1 "
    listavariavel = listavariavel.replace(remover, 'p'+str(numeropedidovariavel) + '|' + str(cpf) + str(QTDO))

    # | POR ESPAÇO E SIRGULA POR ESPAÇO
    remover = ","
    for i in range(0, len(remover)):
        listavariavel = listavariavel.replace(remover[i], "")

    # remover os caracteres da string
    remover = "\'\"][,)( "
    for i in range(0, len(remover)):
        listavariavel = listavariavel.replace(remover[i], "")

    # remover os caracteres da string
    remover = "||||"
    listavariavel = listavariavel.replace(remover, "\n")

    # remover os caracteres da string
    remover = "||"
    listavariavel = listavariavel.replace(remover, "")


    # pular linha 
    listavariavel = '\n'+listavariavel

    # remover os caracteres da string
    remover = "|"
    listavariavel = listavariavel.replace(remover,";")

    # remover os caracteres da string
    remover = "."
    listavariavel = listavariavel.replace(remover,",")




    # abrir ou criar arquivo
    arquivo = open('pedidosdetalhe.csv', 'a',encoding="utf8", newline="")

    # escrever linha
    arquivo.write("%s" % str(listavariavel))

    # fechar
    arquivo.close()



    # gerar relatorio de produtos mais vendidos
    #maisvendido(listavariavel)

    #criarhtml(str(numeropedido))



# gerar relatorio de mais vendidos / produtos mais vendidos
def venda_por_produto(n):
    
    import io
    import codecs

    arq = open('pedidosdetalhe.csv', 'r', encoding="utf8")
    texto = arq.read()

    arq.close()

    dic = dict()

    texto = texto.replace('nome_produto', "")
    # remove letra misnusculas, numeros, espaços, #,#
    b = ",1234567890a b c d e f g h i j k l m n o p q r s t u v w x y z \n :"
    for i in range(0, len(b)):
        texto = texto.replace(b[i], "")


    # remover textos especiais
    texto = texto.replace('SEMCPF', "")
    texto = texto.replace('p', "")
    texto = texto.replace('LIVRE', "")
    texto = texto.replace('COMCOBERTURAEXTRA', "")
    texto = texto.replace('SEMCOBERTURAEXTRA', "")
    texto = texto.replace("",'')


    # separar texto
    listfile = texto.split(';')
    listfile2 = listfile



    for item in listfile:
        Contitem = 0
        for i in listfile2:
            if item == i:
                Contitem = Contitem + 1
                dic[i] = Contitem



    # excluir dic P e DIC ''
    del dic['P']
    del dic['']


    # str do dic em uma variavel
    textodic = str(dic)


    # remover caracteres
    b = '\'}{ '
    for i in range(0, len(b)):
        textodic = textodic.replace(b[i], "")



    textodic = textodic.replace(',', "\n")


    escrever('PRODUTO | QUANTIDADE \n'+textodic)
    continua= input('ENTER PARA CONTINUAR')
    return menu()


# html na tela
def criarhtml(numero):
    pedido = str(numero)
    # linha para salvar
    html = '<!DOCTYPE html>\n<html>\n<head>\n<title>'+str(pedido)+'</title>\n</head>\n<body>\n<h1>'+str(pedido)+'</h1>\n<p>'+str(pedido)+'</p>\n</body>\n</html>'

    # abrir ou criar arquivo
    arquivo = open('index.html', 'a', encoding="utf8")

    # escrever linha
    arquivo.write("%s" % html)

    # fechar
    arquivo.close()

    #abrirfoto('h')

# abrir foto no webbrowser
def abrirfoto(numero):
    import webbrowser
    new = 2;



    #   [1] CHOCOLATE
    if numero == 1:
        url = "https://uploads.metropoles.com/wp-content/uploads/2018/03/22161224/kopenhagen1.jpg"
    #   [2] MISTO
    if numero == 2:
        url = "https://uploads.metropoles.com/wp-content/uploads/2018/03/22161224/kopenhagen1.jpg"
    #   [3] CREME
    if numero == 3:
        url = "https://uploads.metropoles.com/wp-content/uploads/2018/03/22161224/kopenhagen1.jpg"
    #   [4] triplo chocolate Kopenhagen
    if numero == 4:
        url = "https://uploads.metropoles.com/wp-content/uploads/2018/03/22161224/kopenhagen1.jpg"
    #   [5] Kit Kat
    if numero == 5:
        url = "http://s3.id5.com.br/maceioshopping/uploads/2016/07/McFlurryKitKat.jpg"

    # [e] extra
    if numero == 'e':
        url="http://caramelodrama.com/wp-content/uploads/2018/01/melting-choc-istock.jpg"

    # [e] extra
    if numero == 'h':
        url = "file:///home/breno/BRENO/programacao/python/PROJETO%20SORVETERIA/index.html"


    webbrowser.open(url, new=new)
    time.sleep(2)

# gerar preço total
def calcularprecototal(QTDO, SABOR):
    CONTA = float(0)
    if SABOR == 1:  # cho 3rs
        CONTA = float(QTDO * 3.5)
        escrever('preço 3,50')
    if SABOR == 2:  # mis 4rs
        CONTA = float(QTDO * 4)
        escrever('preço 4,00')
    if SABOR == 3:  # cre 5rs
        CONTA = float(QTDO * 4.5)
        escrever('preço 4,50')

    if SABOR == 4:  # cre 5rs
        CONTA = float(QTDO * 8.5)
        escrever('preço 8,50')

    if SABOR == 5:  # cre 5rs
        CONTA = float(QTDO * 9.0)
        escrever('preço 9,00')

    return CONTA

# escrever texto
def escrever(texto):
    texto= str(texto)
    tamanhotexto = len(texto) + 4
    nomecaixa = texto.upper()
    print('~' * tamanhotexto)
    print(" ", nomecaixa)
    print('~' * tamanhotexto)

# sair do sistema
def sair(d):
    # limpar
    limpar()
    menu()

# gerar numero do pedido
def numeropedido(m, h, d, me, an):
    numero = (h + d + me + an) * m
    pedido = str(numero)
    escrever('PEDIDO: ' + pedido)
    return pedido

# inicio do programa
def menu():
    limpar()
    op = ""
    while op == "":
        limpar()
        escrever("NOVA VENDA   [1]")
        escrever("PEDIDO FEITO [2]")
        escrever("PRODUTOS     [3]")
        escrever("relatorios   [4]")
        op = str(input(''))
        if op == "1" or op == "2" or op == "3" or op == "4":
            if op == "2":
                return chamarpedido(1)
            if op == "1":
                return ganhardesconto(1)
            if op == "3":
                return produto(1)
            if op == "4":
                return venda_por_produto(1)
            else:
                op == ""

# tela produto
def produto(p):
    limpar()
    escrever('TELA PRODUTOS')
    escrever("CADASTRAR PRODUTO [1]")
    escrever("EXCLUIR PRODUTO   [2]")
    escrever("VOLTAR            [3]")
    op = str(input(''))
    if op == "1" or op == "2" or op == "3":
        if op == "1":
            return cadastrarproduto(1)
        if op == "2":
            return excluirproduto(1)
        if op == "3":
            return menu()
        else:
            op == ""

# validar nomes
def validarnomes(nome):
    nome = ' '
    c = 0
    while len(nome) < 3:
        if c >= 1:
            escrever('DIGITE CORRETAMENTE')
        nome = input('')
    nomecaixa = nome.upper()
    return nomecaixa

#cadastrar produto
def cadastrarproduto(p):
    limpar()
    escrever('CADASTRAR PRODUTO')
    escrever('NOME DO PRODUTO: ')
    nome = validarnomes(1)

    nome=nome.replace(' ','_')


    valor = 0.0
    while valor < 0.1:
        escrever('VALOR DE VENDA')
        print('EXEMPLO: 5,90')
        valoaux = input('')
        valoaux = valoaux.replace(',','.')
        valor = float(valoaux)


    # opcoes de estoque livre ou com quantidade de estoque
    escrever('cadastrar quantidade do produto? \n      sim [1] | não [2]')
    auxopint = input('')
    opca = int(auxopint)
    while opca < 1 or opca > 2:
        opca = int(input(''))

    if opca == 1:
        escrever('estoque')
        quantidadeestoque = int(input(''))

    if opca == 2:
        quantidadeestoque = 'LIVRE'


    escrever('CONFIRMAR PRODUTO [1]')
    escrever('CANCELAR          [2]')
    op = str(input(''))
    if op == "1" or op == "2":
        if op == "1":
            return confirmarproduto(nome, valor,quantidadeestoque )
        if op == "2":
            return menu()
        else:
            op == ""

# verificar produto no txt
def confirmarproduto(nome, valor, quantidadeestoque):
    with open('produtos.txt', encoding="utf8") as f:
        for l_num, l in enumerate(f, 1):  # percorrer linhas e enumera-las a partir de 1
            if nome in l:  # ver se palavra esta na linha
                escrever(nome + ' JÁ ESTÁ CADASTRADO')
                continua=input('ENTER PARA CONTINUAR')
                cadastrarproduto(1)
                break

        else:  # caso não haja break

            # abrir ou criar arquivo
            arquivo = open('produtos.txt', 'a', encoding="utf8", newline="")

            # criar linha
            liconfirmarprodutonha = str(nome)+'|'+str(valor)+'|'+str(quantidadeestoque)+'\n'


            # escrever linha
            arquivo.write("%s" % liconfirmarprodutonha)

            # fechar
            arquivo.close()

            escrever('PRODUTO CADASTRADO')
            input('ENTER PARA CONTINUAR')

            produto(1)

# exibir produtos
def exibirprodutos(p):
    limpar()
    f = open('produtos.txt', 'r', encoding="utf8")
    n = 0
    for line in f:
        n = n + 1
        print(str(n) +' | '+line)
    return escrever(str(n)+' PRODUTOS CADASTRADOS')

# validar numero de opcao
def validarnumero(numero):
    numero=10
    while numero != 0 or numero != 1 or numero != 2 or numero != 3 or numero != 4 or numero != 5 or numero != 6 or numero != 6 or numero != 8 or numero != 9:
        escrever('OPÇÃO INVALIDA')
        escrever('DIGITE NOVAMENTE')
        auxnumero = str(int(''))
        numero = int(auxnumero)

# add produto no pedido
def addproduto(produto):
    exibirprodutos(1)
    escrever('NUMERO DO PRODUTO: : ')
    index_linha = 0
    index_linha = int(input(''))

    firstLine = ' '
    arq = open('produtos.txt', 'r', encoding="utf8")
    texto = arq.readlines()
    cont = 1
    for linha in texto:
        if index_linha == cont:
            linhadoproduto = linha
            arq.close()



            # logica para exluir caracteres
            # excluir o "pular linha"
            b = "n\n\n"
            for i in range(0, len(b)):
                linhadoproduto = linhadoproduto.replace(b[i], "")








            return linhadoproduto,

        cont = cont + 1
    arq.close()
    return escrever('produto não encontrado')

# excluir produto do txt
def excluirproduto(p):
    exibirprodutos(1)
    escrever('NUMERO DO PRODUTO: : ')
    index_linha = int(input(''))
    index_linha = index_linha - 1
    path = 'produtos.txt'

    with open(path,'r', encoding="utf8") as f:
        texto=f.readlines()
    with open(path,'w', encoding="utf8") as f:
        for i in texto:

            if texto.index(i)==index_linha:
                f.write('')
                escrever('EXCLUIDO!')
            else:
                if index_linha == i:
                    f.write('excluido')
                else:
                    f.write(i)


    menu()

# diretorio do PDF
def meudiretorio(caminho):

    # importar data
    from datetime import datetime
    now = datetime.now()

    # criar diretorio
    #dirTemp = './'+str(now.year)+'/'+str(now.month)+'/'+str(now.day)+'/'
    dirTemp = './PEDIDOS/'
    return dirTemp

# gerar um pdf detalhado do pedido para inprimir e dar para o cliente retira no balcao o seu pedido
def gerarpdfdetalhado(nome, pedido, lista,tsub, tdesc,valortotal, hora):
    from reportlab.pdfgen import canvas

    # organizar texto
    pedidoPDF = 'PEDIDO: ' + str(pedido)
    nomePDF = 'NOME: ' + str(nome)


    sub = 'SUBTOTAL: ' + "%.2f" % float(tsub)
    desc = 'DESCONTO: ' + "%.2f" % float(tdesc)
    valortotalPDF = 'TOTAL: ' +"%.2f" % float(valortotal)




    horaPDF = str(hora)
    listaPDF = 'DESCRIÇÃO: ' + str(lista)

    diretorio=meudiretorio(1)


    # escrever no pdf
    c = canvas.Canvas(diretorio+str(pedido) + '_' + nome + '_' + str(valortotal) + '.pdf')
    c.drawString(440, 800, str(pedidoPDF))
    c.drawString(30, 800, str(nomePDF))
    c.drawString(80, 780, str(sub))
    c.drawString(200, 780, str(desc))
    c.drawString(320, 780, str(valortotalPDF))
    c.drawString(330, 800, str(horaPDF))


    tam = 580
    c.drawString(60, 600, 'DESCRIÇAO: ')


    for add in lista:
        minhalinha = ''
        add.split(';')



        for um in add:
            minhalinha = minhalinha + str(um)

        # remover os caracteres da string
        remover = "||"
        for i in range(0, len(remover)):
            minhalinha = minhalinha.replace(remover, "")


        # remover os caracteres da string
        remover = "\'\"][,)( "
        for i in range(0, len(remover)):
            minhalinha = minhalinha.replace(remover[i], "")



        # remover os caracteres da string
        remover = "|"
        for i in range(0, len(remover)):
            minhalinha = minhalinha.replace(remover[i], " | ")

        # remover os caracteres da string
        remover = "."
        for i in range(0, len(remover)):
            minhalinha = minhalinha.replace(remover[i], ",")



        c.drawString(70, tam, str(minhalinha))
        tam = tam - 20




    # salvar no pdf
    c.save()

# não deixar o programa fechar
continua = True
while continua:
    limpar()
    menu()
