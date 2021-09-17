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
def trantando_os_dados(data):
    from datetime import datetime
    date = datetime.strptime(data, '%d/%m/%Y').date()
    hoje = str(date.today())
    # Transformando strings em números para separar em dia, mês e ano
    dia_de_vencimento = int(data[:2])
    mes_de_vencimento = int(data[3:5])
    ano_de_vencimento = int(data[6:])
    dia_de_hoje = int(hoje[8:])
    mes_de_hoje = int(hoje[5:7])
    ano_de_hoje = int(hoje[:4])
    # Mostrando ao Usuário quando o Título está sendo retirado
    print('O título está sendo Retirado em {}/{}/{}'.format(dia_de_hoje, mes_de_hoje, ano_de_hoje))
    return(dia_de_vencimento,mes_de_vencimento,ano_de_vencimento,dia_de_hoje,mes_de_hoje,ano_de_hoje)
#---------------------------------------------------------------
def calculos(r,dia_de_vencimento,mes_de_vencimento,ano_de_vencimento,dia_de_hoje,mes_de_hoje,ano_de_hoje):
    # Iniciando os cálculos, tomando como base que  o título é comprado antes de cada último dia útil do mês
    # Calculando a quantidade de meses e colocando na fórmula de juros compostos adaptada.
    # O valor do Juros descontado tem que ir diminuindo quanto mais próximo da data de vencimento do título estiver e não o contrário
    anos = ano_de_vencimento - ano_de_hoje
    if anos == 0:
        meses = mes_de_vencimento - mes_de_hoje
    else:
        meses = (12 * (anos)) + abs((mes_de_vencimento - mes_de_hoje))
    # print(meses)
    capital = (meses * 1000) + 10000
    if meses == 0:
        valor = capital
    else:
        print('Se ele ficasse até a Data de Vencimento ele receberia R${:.2f}'.format(capital))
        valor = capital * ((-1 + (r / 100)) ** meses)
    # mostrando ao usuário o valor que vai receber tirando hoje.
    print('Como não ficou, vai receber: R${:.2f}'.format(abs(valor)))
#----------------------------------------------------------------------
def faz():
    r= pede_r()
    data = pede_vencimento()
    dia_de_vencimento,mes_de_vencimento,ano_de_vencimento,dia_de_hoje,mes_de_hoje,ano_de_hoje= trantando_os_dados(data)
    calculos(r,dia_de_vencimento,mes_de_vencimento,ano_de_vencimento,dia_de_hoje,mes_de_hoje,ano_de_hoje)
    if input('Para uma nova execução digite s ') in ('s','S'):
       faz()
#----------------------------------------------------------------------------
faz()