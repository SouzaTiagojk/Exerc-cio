def pede_r():
    try:
        r = float(input('Digite a taxa de juros (apenas o número): '))
        return (abs(r))
    except:
        print('Erro !!! Escreva um número inteiro !!!')
        return pede_r()
#-------------------------------------------------------------------------------
def pede_vencimento():
    try:
        data = str(input('Digite a data vencimento do título no formato XX/XX/XXXX: ')).strip()
        return (data)
    except:
        print('Erro !!! Escreva uma data correta !!!')
        return pede_vencimento()
#---------------------------------------------------------------------------
def pede_compra():
    try:
        compra= str(input('Qual a data de compra do título')).strip()
        return (compra)
    except:
        print('Erro !!! Escreva uma data correta !!!')
        return pede_compra()
#-------------------------------------------------------
def tratando_os_dados(data,compra):
    from datetime import datetime
    date = datetime.strptime(data, '%d/%m/%Y').date()
    hoje = str(date.today())
    dia_de_hoje = int(hoje[8:])
    mes_de_hoje = int(hoje[5:7])
    ano_de_hoje = int(hoje[:4])
    dia_de_vencimento = int(data[:2])
    mes_de_vencimento = int(data[3:5])
    ano_de_vencimento = int(data[6:])
    dia_de_compra = int(compra[:2])
    mes_de_compra = int(compra[3:5])
    ano_de_compra = int(compra[6:])
    # Mostrando ao Usuário quando o Título está sendo retirado
    print('O título está sendo Retirado em {}/{}/{}'.format(dia_de_hoje, mes_de_hoje, ano_de_hoje))
    return(dia_de_vencimento,mes_de_vencimento,ano_de_vencimento,dia_de_hoje,mes_de_hoje,ano_de_hoje,dia_de_compra,mes_de_compra,ano_de_compra)
#---------------------------------------------------------------
def calculos (r,dia_de_vencimento,mes_de_vencimento,ano_de_vencimento,dia_de_hoje,mes_de_hoje,ano_de_hoje,dia_de_compra,mes_de_compra,ano_de_compra):
    #Dessa vez, vou considerar o exercício que o juros desconta sobre o valor que ele já ganhou, como juros simples
    #Ou seja, o valor que ele ganhou até aqueele momento com o título menos o juros que vai descontar dele
    #Vamos lá !
    anos = ano_de_hoje - ano_de_compra
    if anos == 0:
        meses = mes_de_hoje - mes_de_compra
    else:
        meses = (12 * (anos)) + abs(mes_de_hoje - mes_de_compra)
    if dia_de_vencimento== dia_de_hoje and mes_de_vencimento == mes_de_hoje and ano_de_vencimento== ano_de_hoje:
        valor= (1000*meses)+10000
    else:
        capital= 1000*meses
        valor= capital-(capital*(r/100))
        print('Você ganhou até agora R${:.2f} mas com o juros a ser descontado'.format(capital))
    print('Você vai receber: R${:.2f}'.format(valor))

#----------------------------------------------------------------------
def faz():
    r= pede_r()
    data = pede_vencimento()
    compra = pede_compra()
    dia_de_vencimento,mes_de_vencimento,ano_de_vencimento,dia_de_hoje,mes_de_hoje,ano_de_hoje,dia_de_compra,mes_de_compra,ano_de_compra= tratando_os_dados(data,compra)
    calculos(r,dia_de_vencimento,mes_de_vencimento,ano_de_vencimento,dia_de_hoje,mes_de_hoje,ano_de_hoje,dia_de_compra,mes_de_compra,ano_de_compra)
    if input('Para uma nova simulação digite s ') in ('s','S'):
       faz()
#----------------------------------------------------------------------------
faz()