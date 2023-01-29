# Gabriele Namie Takaki Honda - TIA: 32088991
# Guilherme de Souza Valente - TIA: 32034008 
# Rafael Junqueira Pezeiro - TIA: 32035901
# Vitória Karpovas Chisman - TIA: 32008554

# importando as bibliotecas necessárias
import pygame,sys  
from pygame.locals import *
from pygame import mixer
import random

pygame.init()

# lista de cores para a tabela do jogo
Cores=[]
Cores=[(51, 204, 204),(204, 0, 0),(102, 0, 255),(0, 153, 51),(255, 153, 0),(179, 0, 134),(255, 51, 187),(0, 0, 102),(51, 51, 0), (204, 51, 0), (0, 102, 102),(255, 51, 255), (255, 255, 102),(230, 204, 255),(255, 204, 229),(179, 0, 89),(102, 0, 102)]


# input dos nomes dos jogadores
jogador_O=input("Insira o nome do jogador ""O"": ")
jogador_x=input("Insira o nome do jogador ""X"": ")


#Importando possiveis pares de imagens X e Y
ImgsO=[]
ImgsO=["O1.png","O2.png","O3.png","O4.png"]
Time=random.randint(0,3)
ImgsX=[]
ImgsX=["X1.png","X2.png","X3.png","X4.png"]


# criando a tela do pygame
tela = pygame.display.set_mode((610,550)) 
pygame.display.set_caption("Jogo da Velha")

# importando as imagens gerais
xis = pygame.image.load("xis.png").convert_alpha()
bola = pygame.image.load("bola.png").convert_alpha()
smiley = pygame.image.load("smiley.png").convert_alpha()
integrantes=pygame.image.load("int.png").convert_alpha()


#Pegando imagens dos jogadores;
JogO=pygame.image.load(ImgsO[Time]).convert_alpha()
JogX=pygame.image.load(ImgsX[Time]).convert_alpha()


# background music
mixer.music.load("Wii.wav")
mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

#Aplauso
aplauso=mixer.Sound("cheer3.wav")

aplauso.set_volume(0.2)

#Empate
eempate=mixer.Sound("Boliche.wav")

eempate.set_volume(0.2)


# fonte do texto no jogo
text = pygame.font.SysFont("Arial.ttf", 32)

FonteOBG = pygame.font.SysFont("Arial.ttf", 60)



aviso = pygame.Surface((0,0))
pontosJogadorBola = pygame.Surface((0,0))
pontosJogadorXis = pygame.Surface((0,0))




continuar = True
cont=True
terminou = False
comecou = False

jogadorBola = True
jogadorXis = False

posX = -50
posY = -50

contadorPontosBola = 0
contadorPontosXis = 0

casas = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
posicoes = [(80,45),(250,45),(430,45),(80,180),(250,180),(430,180),(80,325),(250,325),(430,325)]

jogada = True

contJogadas = 0

def preencherCasas():
    for i in range(len(casas)):
            if casas[i] == 0:
                tela.blit(bola,(posicoes[i]))
                    
            elif casas[i] == 1:
                tela.blit(xis,(posicoes[i]))


#Cores das Linhas
c1=random.randint(0,16)

c2=random.randint(0,16)
while c2==c1:
  c2=random.randint(0,16)
  
c3=random.randint(0,16)
while c3==c2 or c3==c1:
  c3=random.randint(0,16)

c4=random.randint(0,16)
while c4==c3 or c4==c2 or c4==c1:
  c4=random.randint(0,16)
                

# montando o tabuleiro                
                
def montarTabuleiro():
    tela.fill((255,255,255))
    tela.blit(aviso,(240,25))
    tela.blit(novoJogo,(30,500))
    tela.blit(pontosJogadorBola,(60,10))
    tela.blit(ss,(250,500))
    tela.blit(nn,(320,500))
    
    tela.blit(JogO,(10,0))
    tela.blit(JogX,(440,0))
    
    tela.blit(pontosJogadorXis,(490,10))
    pygame.draw.line(tela,Cores[c1],(200,50),(200,420),5)
    pygame.draw.line(tela,Cores[c2],(80,150),(530,150),5)
    pygame.draw.line(tela,Cores[c3],(400,50),(400,420),5)
    pygame.draw.line(tela,Cores[c4],(80,300),(530,300),5)
    


while(continuar):
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()      

    
        
        posX = pygame.mouse.get_pos()[0]
        posY = pygame.mouse.get_pos()[1]
        
    
        teclas  = pygame.key.get_pressed()
    
        if terminou == False and comecou == True:
            if ((posX >= 81 and posX <= 195) and (posY >= 50 and posY <= 144)): 
                if casas[0] == -1:
                    if (pygame.mouse.get_pressed()[0] or teclas[K_LEFT]) and jogadorBola == True:
                        casas[0] = 0
                        jogadorBola = False
                        jogadorXis = True
                        contJogadas+=1
                        
                    elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
                        casas[0] = 1
                        jogadorBola = True
                        jogadorXis = False
                        contJogadas +=1
                        

            if ((posX >= 203 and posX <= 398) and (posY >= 50 and posY <= 144)):    
                if casas[1] == -1:
                    if pygame.mouse.get_pressed()[0] and jogadorBola == True:
                        casas[1] = 0
                        jogadorBola = False
                        jogadorXis = True
                        contJogadas+=1
                        
                    elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
                        casas[1] = 1
                        jogadorBola = True
                        jogadorXis = False
                        contJogadas +=1
                                            
                    
            if ((posX >= 404 and posX <= 531) and (posY >= 50 and posY <= 144)):    
                if casas[2] == -1:
                    if pygame.mouse.get_pressed()[0] and jogadorBola == True:
                        casas[2] = 0
                        jogadorBola = False
                        jogadorXis = True
                        contJogadas+=1
                        
                    elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
                        casas[2] = 1
                        jogadorBola = True
                        jogadorXis = False
                        contJogadas +=1
                        

            if ((posX >= 81 and posX <= 195) and (posY >= 153 and posY <= 295)):    
                if casas[3] == -1:
                    if pygame.mouse.get_pressed()[0] and jogadorBola == True:
                        casas[3] = 0
                        jogadorBola = False
                        jogadorXis = True
                        contJogadas+=1
                        
                    elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
                        casas[3] = 1
                        jogadorBola = True
                        jogadorXis = False
                        contJogadas +=1
                        


            if ((posX >= 203 and posX <= 398) and (posY >= 153 and posY <= 295)):   
                if casas[4] == -1:
                    if pygame.mouse.get_pressed()[0] and jogadorBola == True:
                        casas[4] = 0
                        jogadorBola = False
                        jogadorXis = True
                        contJogadas+=1
                        
                    elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
                        casas[4] = 1
                        jogadorBola = True
                        jogadorXis = False
                        contJogadas +=1
                        

            if ((posX >= 404 and posX <= 531) and (posY >= 153 and posY <= 295)):   
                if casas[5] == -1:
                    if pygame.mouse.get_pressed()[0] and jogadorBola == True:
                        casas[5] = 0
                        jogadorBola = False
                        jogadorXis = True
                        contJogadas+=1
                        
                    elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
                        casas[5] = 1
                        jogadorBola = True
                        jogadorXis = False
                        contJogadas +=1
                        

            if ((posX >= 81 and posX <= 195) and (posY >= 304 and posY <= 420)):    
                if casas[6] == -1:
                    if pygame.mouse.get_pressed()[0] and jogadorBola == True:
                        casas[6] = 0
                        jogadorBola = False
                        jogadorXis = True
                        contJogadas +=1
                        
                    elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
                        casas[6] = 1
                        jogadorBola = True
                        jogadorXis = False
                        contJogadas +=1
                        

            if ((posX >= 203 and posX <= 398) and (posY >= 304 and posY <= 420)):   
                if casas[7] == -1:
                    if pygame.mouse.get_pressed()[0] and jogadorBola == True:
                        casas[7] = 0
                        jogadorBola = False
                        jogadorXis = True
                        contJogadas +=1
                        
                    elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
                        casas[7] = 1
                        jogadorBola = True
                        jogadorXis = False
                        contJogadas +=1
                        

            if ((posX >= 404 and posX <= 531) and (posY >= 304 and posY <= 420)):   
                if casas[8] == -1:
                    if pygame.mouse.get_pressed()[0] and jogadorBola == True:
                        casas[8] = 0
                        jogadorBola = False
                        jogadorXis = True
                        contJogadas +=1
                        
                    elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
                        casas[8] = 1
                        jogadorBola = True
                        jogadorXis = False
                        contJogadas +=1
    
            if (casas[0] == 1 and casas[1] == 1 and casas[2] == 1) or (casas[3] == 1 and casas[4] == 1 and casas[5] == 1) or (casas[6] == 1 and casas[7] == 1 and casas[8] == 1) or (casas[0] == 1 and casas[3] == 1 and casas[6] == 1) or (casas[1] == 1 and casas[4] == 1 and casas[7] == 1) or (casas[2] == 1 and casas[5] == 1 and casas[8] == 1) or (casas[0] == 1 and casas[4] == 1 and casas[8] == 1) or (casas[2] == 1 and casas[4] == 1 and casas[6] == 1):
                aviso = text.render(f' {jogador_x} Ganhou', True, (0, 0, 0))
                aplauso.play()
                terminou = True
                comecou=False
                cont=False
                contadorPontosXis +=1
                pontosJogadorXis = text.render(f' {jogador_x} = ' +str(contadorPontosXis), True, (0,0,255)) 
                
            
            
            elif (casas[0] == 0 and casas[1] == 0 and casas[2] == 0) or (casas[3] == 0 and casas[4] == 0 and casas[5] == 0) or (casas[6] == 0 and casas[7] == 0 and casas[8] == 0) or (casas[0] == 0 and casas[3] == 0 and casas[6] == 0) or (casas[1] == 0 and casas[4] == 0 and casas[7] == 0) or (casas[2] == 0 and casas[5] == 0 and casas[8] == 0) or (casas[0] == 0 and casas[4] == 0 and casas[8] == 0) or (casas[2] == 0 and casas[4] == 0 and casas[6] == 0):
                    aviso = text.render(f' {jogador_O} ganhou!', True, (0, 0, 0))
                    aplauso.play()
                    terminou = True
                    comecou=False
                    cont=False
                    contadorPontosBola +=1
                    pontosJogadorBola = text.render(f' {jogador_O} = ' +str(contadorPontosBola), True, (0,0,255))
                    
                    
            elif contJogadas >= 9:
                    aviso = text.render("Empate", True, (0, 0, 0))
                    eempate.play()
                    terminou = True
                    terminou = True
                    comecou=False
                    cont=False
        
    
        
    
    if comecou==False and cont==True:
        novoJogo = text.render("Começar partida", True, (0,0,0))
        novoJogoRect = novoJogo.get_rect().move(30,500)
        ss=text.render("", True, (0,0,0))
        nn=text.render("", True, (0,0,0))
        Vencedor = text.render("", True, (0,0,0))

        
        siRect= ss.get_rect().move(220,500)
        noRect= nn.get_rect().move(260,500)
 

    
    elif comecou==True:
        novoJogo = pygame.Surface((0,0))
        ss=text.render("", True, (0,0,0))
        nn=text.render("", True, (0,0,0))
        pontosJogadorBola = text.render(f' {jogador_O} = ' +str(contadorPontosBola), True, (0,0,255))
        pontosJogadorXis = text.render(f' {jogador_x} = ' +str(contadorPontosXis), True, (0,0,255)) 
        
    if novoJogoRect.collidepoint(pygame.mouse.get_pos()) and comecou==False:
        novoJogo = text.render("Começar partida", True, (255,0,0))
        if pygame.mouse.get_pressed()[0]:
            comecou=True
            terminou=False
            contJogadas=0
            casas = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
            aviso = pygame.Surface((0,0))
            
    if cont==False:
            novoJogo = text.render("Jogar novamente?", True, (0,0,0))
            ss=text.render("Sim", True, (0,0,0))
            nn=text.render("Não", True, (0,0,0))
 
            tela.blit(ss,(250,500))
            tela.blit(nn,(320,500))  

            siRect= ss.get_rect().move(250,500)
            noRect= nn.get_rect().move(320,500)
            novoJogoRect = novoJogo.get_rect().move(30,500)
        


    if siRect.collidepoint(pygame.mouse.get_pos()) and cont==False:
        ss = text.render("Sim", True, (255,0,0))
        if pygame.mouse.get_pressed()[0]:
            cont=True
            comecou=True
            terminou=False
            contJogadas=0
            casas = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
            aviso = pygame.Surface((0,0))
            
    if noRect.collidepoint(pygame.mouse.get_pos()) and cont==False:
        nn = text.render("Não", True, (255,0,0))
        if pygame.mouse.get_pressed()[0]:
            Saidera=True
            continuar=False

                
            
            

            
            

                        
    montarTabuleiro()

    preencherCasas()

            
    pygame.display.flip()

while Saidera==True:

    


    
    tela.fill((255,255,255))
    
    if contadorPontosBola > contadorPontosXis:
        Vencedor = text.render(f'Parabéns {jogador_O}!!', True, (0,0,0))
        Perdedor = text.render(f'Tudo bem {jogador_x} segundo lugar não é tão ruim', True, (0,0,0))

        

    elif contadorPontosXis > contadorPontosBola:
        Vencedor = text.render(f'Parabéns {jogador_x}!!', True, (0,0,0))
        Perdedor = text.render(f'Tudo bem {jogador_O} segundo lugar não é tão ruim', True, (0,0,0))


    else:
        Vencedor = text.render(f'Que pena, temos um empate!!', True, (0,0,0))
        Perdedor = text.render(f'Pelo menos não teve um perdedor!', True, (0,0,0))
            
    tela.blit(Vencedor,(20,10))
    tela.blit(Perdedor,(20,500))
    Obrigado= FonteOBG.render("Obrigado por jogar!", True, (0,0,0))
    tela.blit(Obrigado,(100,120))
    tela.blit(smiley,(240,210))



    tela.blit(integrantes,(310,300))
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()

