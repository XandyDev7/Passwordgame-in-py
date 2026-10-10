
# vamos criar uma FUNCAO para CADA uma das REGRAS
# cada função recebe a senha e retorna TRUE se atendeu ou FALSE se não atendeu
# as funcoes serão usada no while principal para manter o jogo funcionando
# senha é o paramento da funcao regra 1
# R1: ter pelo menos 5 caracteres
#12 regras
'''
letra maiuscula
character especial
the digit in your password must add up to 25
roman numerals'''
def regra1(senha):
    comp = len(senha)
    if comp < 5:
        print("Erro regra1: sua senha precisa ter pelo menos 5 caracteres!")
        return False
    else:
        print(f"Ok regra1: sua senha tem {comp} caracteres.")
        return True

# R2: ter pelo menos um número
def regra2(senha):
    for letra in senha:
        if letra.isdigit():
            print("Ok regra2: sua senha contém um número.")
            return True  # Achou um número, pode retornar True direto
    
    # Se o loop terminar sem encontrar nenhum número:
    print("Erro regra2: sua senha precisa conter um número.")
    return False

def regra3 (senha):
    if senha.islower():
        print("Erro regra3: sua senha precisa conter pelo menos uma letra maiúscula.")
        return False
    else:
        print("Ok regra3: sua senha contém pelo menos uma letra maiúscula.")
        return True
  



 #My order 

'''def regra4 (senha):
    lista = ["36", "49", "64", "100", "81", "121","144"]
    for item in lista:
        if item in lista:
            print(f"Erro regra4: sua senha precisa conter um quadrado perfeito maior que 6 ao quadrado e menor que 12 ao quadrado.")
            return  True
        else:
            print(f"Erro regra4: sua senha precisa conter um quadrado perfeito maior que 6 ao quadrado e menor que 12 ao quadrado.")
            return False '''
def regra4(senha):
     
     quadrados = ["49", "64", "81", "100", "121"]
    
     for item in quadrados:
          if item in senha:  # Testa se o número está DENTRO da senha digitada
              print(f"Ok regra4: sua senha contém o quadrado perfeito {item}.")
              return True    #  Encerra retornando True
            
     print("Erro regra4: sua senha precisa conter um quadrado perfeito maior que 6² e menor que 12².")
     return False


def regra5(senha):
         especial = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
         for item in especial:
             if item in senha:
                 print("Ok regra5: sua senha contém pelo menos um caractere especial.")
                 return True
                

     
         return False


def regra6(senha):
    soma =0 
    for caracter in senha:
        if caracter.isdigit():
            soma =soma + int(caracter)
    if soma == 25:
        print("Ok regra6: a soma dos dígitos da sua senha é igual a 25.")
        return True
    else:
        print(f"Erro regra6: a soma dos dígitos da sua senha é {soma}, mas precisa ser igual a 25.") 
    return False

def regra7(senha):
    
    one_piece = [ "alabasta", "skypiea", "water7", "enieslobby", "thrillerbark", "sabaody", "marineford", "eastblue", "amazonlily", "impeldown"]
    
    senha_minuscula = senha.lower()
    
    for item in one_piece:
        if item in senha_minuscula:
            print("Ok regra7: sua senha contém um arco do pré-timeskip de One Piece.")
            return True
            
    print("Erro regra7: sua senha precisa conter um arco do pré-timeskip de One Piece.")
    return False


def regra8(senha):

 return False 

ganhou = False
while not ganhou:
    senha = input("Qual sua senha: ")
    if regra1(senha):
        if regra2(senha):
            if regra3(senha):
               if regra4(senha):
                 if regra5(senha):
                     if regra6(senha):
                          if regra7(senha):
                           ganhou = True
                           print("Parabéns! Senha aprovada!")
                
