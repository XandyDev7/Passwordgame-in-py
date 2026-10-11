
# vamos criar uma FUNCAO para CADA uma das REGRAS
# cada função recebe a senha e retorna TRUE se atendeu ou FALSE se não atendeu
# as funcoes serão usada no while principal para manter o jogo funcionando
# senha é o paramento da funcao regra 1
# R1: ter pelo menos 5 caracteres
#12 regras

import random
import datetime

# Sorteia o número secreto da Regra 7 uma única vez antes do jogo começar
numero_sorteado = random.randint(11, 99)

def regra1(senha):
    comp = len(senha)
    if comp < 5:
        print("Erro regra1: sua senha precisa ter pelo menos 5 caracteres!")
        return False
    else:
        print(f"Ok regra1: sua senha tem {comp} caracteres.")
        return True

def regra2(senha):
    for letra in senha:
        if letra.isdigit():
            print("Ok regra2: sua senha contém um número.")
            return True  
    print("Erro regra2: sua senha precisa conter um número.")
    return False

def regra3(senha):
    if senha.islower():
        print("Erro regra3: sua senha precisa conter pelo menos uma letra maiúscula.")
        return False
    else:
        print("Ok regra3: sua senha contém pelo menos uma letra maiúscula.")
        return True

def regra4(senha):
    quadrados = ["49", "64", "81", "100", "121"]
    for item in quadrados:
        if item in senha:
            print(f"Ok regra4: sua senha contém o quadrado perfeito maior que 6² e menor que 12²: {item}.")
            return True  # Encontrou = Sucesso,sem usar else
            
    print("Erro regra4: sua senha precisa conter um quadrado perfeito maior que 6² e menor que 12².")
    return False

def regra5(senha):
    especial = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    for item in especial:
        if item in senha:
            print("Ok regra5: sua senha contém pelo menos um caractere especial.")
            return True
    print("Erro regra5: sua senha precisa conter pelo menos um caractere especial.")
    return False

def regra6(senha):
    soma = 0 
    for caracter in senha:
        if caracter.isdigit():
            soma = soma + int(caracter)
            
    if soma == 25:
        print("Ok regra6: a soma dos dígitos da sua senha é igual a 25.")
        return True
    else:
        print(f"Erro regra6: a soma dos dígitos da sua senha é {soma}, mas precisa ser igual a 25.") 
        return False

def regra7(senha):
    texto_secreto = str(numero_sorteado)
    if texto_secreto in senha:
        print(f"Ok regra7: sua senha contém o número sorteado, ele é {texto_secreto}.")
        return True
    else:
        print(f"Erro regra7: sua senha não contém o número sorteado, ele é {texto_secreto}.")
        return False 

def regra8(senha):
    romanos = ["II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    for item in romanos:
        if item in senha:
            print(f"Ok regra8: sua senha contém o numeral romano {item}.")
            return True
            
    print("Erro regra8: sua senha precisa conter um numeral romano de II a X.")
    return False

def regra9(senha):
    one_piece = ["alabasta", "skypiea", "water7", "enieslobby", "thrillerbark", "sabaody", "marineford", "eastblue", "amazonlily", "impeldown"]
    senha_minuscula = senha.lower()
    
    for item in one_piece:
        if item in senha_minuscula:
            print("Ok regra9: sua senha contém um arco do pré-timeskip de One Piece.")
            return True
            
    print("Erro regra9: sua senha precisa conter um arco do pré-timeskip de One Piece.")
    return False

def regra10(senha):
    bronze_boys = ["seiya", "shun", "hyoga", "shiryu", "ikki"]
    senha_minuscula = senha.lower()
    
    for item in bronze_boys:
        if item in senha_minuscula:
            print(f"Ok regra10: sua senha contém um dos bronzeboys (protas do Cavaleiro do Zodíaco).")
            return True
            
    print("Erro regra10: sua senha precisa conter um dos protas de  Cavaleiros do Zodíacou ).")
    return False

def regra11(senha):
    data_atual = datetime.datetime.now()
    ano_atual = str(data_atual.year)
    
    if ano_atual in senha:
        print(f"Ok regra11: sua senha contém o ano atual {ano_atual}.")
        return True
    else:
        print(f"Erro regra11: sua senha precisa conter o ano atual {ano_atual}.")
        return False

def regra12(senha):
    if "alexandre" in senha.lower():
        print("Ok regra12: sua senha contém o nome do criador do jogo, meus parabens pequena criatura'.")
        return True
    else:
        print("Erro regra12: sua senha precisa conter o primeiro  nome do criador do jogo (euzinho).")
        return False

# Estrutura  do jogo
ganhou = False
while not ganhou:
    senha = input("Qual sua senha ?")
    
    if regra1(senha):
        if regra2(senha):
            if regra3(senha):
                if regra4(senha):
                    if regra5(senha):
                        if regra6(senha):
                            if regra7(senha):
                                if regra8(senha):
                                    if regra9(senha):
                                        if regra10(senha):
                                            if regra11(senha):
                                                if regra12(senha):
                                            
                                                      ganhou = True
                                                      print("Parabéns! Senha aprovada em todas as 12 regras!")
