def lin():
    print(f'{"--" * 40}')


# PEGANDO INFORMAÇÕES DO USUARIO!
print(f'''REQUESITOS PARA TER UMA SENHA SEGURA:
1 - TER NO MINIMO 4 NUMEROS NA SUA SENHA.
2 - TER O TAMANHO TOTAL DE 8 CARACTERES.
3 - TER MAIS QUE 5 LETRAS NA SUA SENHA.
{'--' * 34}
OBS: ESSES SÃO OS REQUESITOS QUE EU DESENVOLVI PARA ESSE PROJETO.  ''')
lin()
senha = str(input('Digite Sua Senha: ')).lower()
# -----------------------------------------------------------------------------------------------------------------------
# ARMAZENADO DADOS A SEREM ANALIZADOS!
num = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
letra = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
         'x', 'y', 'z']

lugar = ['', '', '']
contLEN = 8
cont = PARAR = CONT_NUM = CONT_LETRA2 = CONT_LETRA = 0
# -----------------------------------------------------------------------------------------------------------------------
# INICIO DA ANALISE DE DADOS!
while PARAR != len(senha):
    # VERIFICANDO SE CONTEM NUMEROS NA SENHA!
    if senha[PARAR] in num:
        cont += 1
        CONT_NUM += 1
    # ---------------------------------------
    # VERIFICANDO SE CONTEM LETRAS NA SENHA!
    if senha[PARAR] in letra:
        CONT_LETRA += 1
        CONT_LETRA2 += 1
        contLEN -= 1
    # ---------------------------------------
    PARAR += 1

# VARIAVEIS DO TIPO BOOL
CONT_NUM = True if CONT_NUM >= 4 else False  # VERIFICAMDO SE HÁ OU NÃO MAIS DE 4 NUMEROS NA SENHA.
# VALOR_NUMERICO = True if CONT_NUM == True else False
QUANTIDADE_LETRAS = False if CONT_LETRA <= 5 else True  # VERIFICANDO SE HÁ OU NÃO MAIS QUE 5 LETRAS NA SENHA.
TAMANHO_DA_SENHA = True if len(senha) >= 8 else False  # ANALISANDO TAMANHO DA SENHA.
# ----------------------------------------------------------------------------------------------------------
# APOS ANALISAR OS VALORES ARMAZENEI ELES DENTRO DE UMA UNICA VARIAVEL
RESULTADO = True if (CONT_NUM) is (True) and (TAMANHO_DA_SENHA) is (True) and (QUANTIDADE_LETRAS) is (
    True) == True else False
# ----------------------------------------------------------------------------------------------------------

if RESULTADO == True:
    lin()
    print('SENHA SEGURA!')
# MOSTRANDO OS DADOS EM FORMA DE TABELA.
# OBS: NÃO UTILIZEI NENHUMA BIBLIOTECA, APENAS UTILIZEI FERRAMENTAS QUE O PYTHON DISPONIBILIZA.
elif RESULTADO == False:
    lugar[0] = 'QUANTIDADE DE NUMEROS OK.' if CONT_NUM == True else f'{"FALTA" if 4 - cont == 1 else "FALTAM"} ' \
                                                                    f'{4 - cont if 4 - cont < 4 else " NO MÍNIMO 4"} {"NUMERO" if 4 - cont == 1 else "NUMEROS"} NA SUA SENHA.'

    # ----------------------------------------------------------------------------------------------------------------------------
    lugar[1] = 'TAMANHO DA SENHA OK.' if TAMANHO_DA_SENHA == True else f'{"FALTA" if 8 - len(senha) == 1 else "FALTAM"}' \
                                                                       f' {8 - len(senha) if len(senha) < 8 else "NO MINIMO 7"} {"CARACTERE" if 8 - len(senha) == 1 else "CARACTERES"} NA SUA SENHA PARA O TAMANHO TOTAL.'

    # --------------------------------------------------------------------------------------------------------------------------------------------------------
    lugar[
        2] = 'QUANTIDADE DE LETRAS OK.' if QUANTIDADE_LETRAS == True else f'{"FALTA" if 5 - CONT_LETRA2 == 1 else "FALTAM"}' \
                                                                          f' {5 - CONT_LETRA2 if 5 >= CONT_LETRA2 <= 5 else "NO MINIMO 4"} {"CARACTERE" if 5 - CONT_LETRA2 == 1 else "CARACTERES"} DE TEXTO NA SUA SENHA.'

    # ------------------------------------------------------------------------------------------------------
    print(
        f'{"--" * 40}\nQUANTIDADE DE NUMEROS: {lugar[0]}\n{"--" * 40}\nTAMANHO TOTAL DA SENHA: {lugar[1]}\n{"--" * 40}\nQUANTIDADE DE LETRAS: {lugar[2]}\n{"--" * 40}')
# ------------------------------------------------------------------------------------------------------
