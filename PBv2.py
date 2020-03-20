#Pigs and Bulls T2
#Beatriz Alvito n32436 e Pedro Nunes n 31240 


import random 
def randomnumber(): #gerar um numero random int de 4 algarismos
    a = 0
    lista = []
    number = ""
    while a<4:
        c = int (10*random.random()) #numero do algarismo 0 até ao 9
        if c not in lista:
            lista.append(c)
            a+=1
    for i in range(len(lista)):
        r =str(lista[i])         #tranformar a lista em str
        number+=r
    return number

def versao1():
    number = randomnumber() #para chamar a função para ser usada nesta função
    print(number) #para ver o numero random gerado na fase de desenvolvimento
    codigo = ""
    solucao = []
    tentativas = 0 #inicializar
    q = [ ]
    while codigo != number: #enquanto o codigo inserido for diferente do numero gerado faz
        pig = 0
        bull = 0
        codigo = str(input("Código?? "))
        if codigo == number: #se o codigo inserido for igual ao numero gerado
            print('Acertou!')
            x = "T{a}: {b}, 4B".format(a=tentativas, b=codigo)
        else:
            for i in range(len(number)): #numero certo de digitos
                if codigo[i] == number[i]:
                    bull +=1
            for i in range(len(number)): #numero fora do sitio
                if codigo[i] in number and codigo[i] !=number[i]:
                    pig +=1

            if bull>0:
                print(bull,"B")
                x = "T{a}: {b}, {c}B".format(a=tentativas, b=codigo, c=bull)
            elif pig>0:
                print(pig,"P")
                x = "T{a}: {b}, {d}P".format(a=tentativas, b=codigo, d = pig)
            elif pig>0 and bull>0:
                print(bull,"B",pig,"P")
                x = "T{a}: {b}, {c}B {d}P".format(a=tentativas, b=codigo, c=bull, d = pig)
            q.append(x)
        tentativas +=1

        print(x)    
    print("Fez",tentativas, "tentativas")

def versao2():
    boole=True
    while boole:
        l = str (input("Qual o código pensado(apenas para ser mais fácil comparar): "))
        if len(l) ==4 and l[0]!=l[1] and l[0]!=l[2] and l[0]!=l[3] and l[1]!=l[2] and l[1]!=l[3] and l[2]!=l[3]: #garantir que sao 4 digitos e todos !=
            boole=False
        else:
            print("Meta um codigo valido")
            
    int_l=[int(l[0]),int(l[1]),int(l[2]),int(l[3])]     #transforma a str em int
    number = randomnumber()                             #chama o randomnumber
    print(number)                                 
    tenta_achar(l,number)                   

def tenta_achar(user_input,pc_try):
    strings=[]
    temp=[]
    lista_tentativas=[]
    new_strings=[0,0,0,0]
    b = 0
    count = 0
    numerosatentar = [0,1,2,3,4,5,6,7,8,9]   #lista dos numeros possiveis
    for i in pc_try:
        strings.append(int(i))  #cria a lista com os inteiros
    for j in numerosatentar:
        if j not in strings:
            temp.append(j)      #cria uma lista temporaria com os numeros que podem ser usados
    while b!='4':
        count +=1
        print("Numero a achar: ",user_input)
        print("Numero do Computador: ",strings)
        p = input("Qual o numero de porcos: ")
        b = input("Qual o numero de touros: ")
        if p == '0' and b == '0':    #senao existir nenhum P nem nenhum B apaga esses numeros 
            strings[0] = temp[0]       #troca os numeros
            strings[1] = temp[1]
            strings[2] = temp[2]
            strings[3] = temp[3]
            del temp[0:4]               #elimina os numeros "velhos"
        
            
        elif (p == '4' and b == '0') or (p=='2' and b=='2') or (p=='3' and b=='1') :
            random.shuffle(strings) #muda os numeros entre si
           
            #print("lista tentativas: ", listatentativas)
            
        elif ((p == '0' and b == '1') or (p == '0' and b == '2') or (p=='0' and b == '3') or (p=='1' and b == '0')or (p=='1' and b == '1') or (p=='1' and b =='2') or (p=='2' and b == '0') or (p=='2' and b == '1') or (p=='3' and b == '0')) :
            #listatentativas.append(strings)
            number= randomnumber()                   #este elif trata dos casos mais dificies de P n B 
            for i in number:
                strings.append(int(i))          #tenta gerar outro numero e nunca volta ao mesmo que já esteve
            del strings[0:4]
        elif b=='4':
            break
        else:
            print("Input invalido") #quando se faz um input errado - numero B or P

    print("Bom jogo!! O computador acertou \n " )
    print("Tentou:", count, "vezes")        
        
            
def ajuda(certo,tentativa):  #esta função foi usada no desenvolvimento, mas não está a ser usada
    porcos = 0
    touros = 0
    for i in range(len(certo)):
        if certo[i]==tentativa[0]:
            if i == 0:
                touros +=1
            else:
                porcos +=1
        elif certo[i]==tentativa[1]:
            if i == 1:
                touros +=1
            else:
                porcos +=1
        elif certo[i]==tentativa[2]:
            if i == 2:
                touros +=1
            else:
                porcos +=1
        elif certo[i]==tentativa[3]:
            if i == 3:
                touros +=1
            else:
                porcos +=1
    return (porcos,touros)

                

def menu():    #apresenta o menu de jogo e chama a função correspondente ao numero inserido pelo user
    print("Jogo Pigs and Bulls!!")
    menu= "1 - Jogar versão 1 \n2 - Jogar versão 2 \n3 - Sair \n"

    while True:
        print(menu)
        v = input("Insira a sua opção: ")
        if (v=="3") or (v=="Opção 3") or (v=="Sair"):
            break

        elif (v=="Opção 1") or (v=="1"):
            versao1()

        elif (v=="Opção 2") or (v=="2"):
            versao2()

        else:
            print("Opção incorreta\n")
 

menu()
        

        
    
