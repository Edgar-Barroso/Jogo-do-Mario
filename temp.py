import pygame
import random


largura = 1000
altura = 500
frames = 60
cor_branca = (255,255,255)
cor_vermelho = (255,0,0)
cor_prata = (192,192,192)
cor_amarelo = (255,255,0)
cor_verde = (0,255,0)
solo = 340
velocidade_mapa = 10


class Cano(pygame.sprite.Sprite):
    def __init__(self,imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = 320,largura+random.randint(0, 1000)
    def update(self,superficie):
        superficie.blit(self.imagem,self.rect)
    def mover(self):
        self.rect.move_ip(-velocidade_mapa,0)
    def recriar(self):
        if self.rect.left < -200:
            self.rect.top, self.rect.left = 320,largura+random.randint(0, 1000)
            
            
        
class Player(pygame.sprite.Sprite):
    def __init__(self,imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (solo,100)
        
        
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    
    def update(self,superficie):
        superficie.blit(self.imagem,self.rect)

def colisao(player,rect):
    if player.rect.colliderect(rect):
        return True
    else:
        return False

def main(frames):
    pygame.init()
    tela = pygame.display.set_mode([largura,altura])

    relogio = pygame.time.Clock()
    
    img_mario = pygame.image.load('mario.png').convert_alpha()
    jogador = Player(img_mario)
    
    img_fundo1 = pygame.image.load('fundo.png').convert_alpha()
    img_fundo2 = pygame.image.load('fundo.png').convert_alpha()
    cano = pygame.image.load('cano.png').convert_alpha()
    
    vx,vy = 0,0
    velocidade = 20
    uppress = False
    sair = False
    x=0
    y=largura
    cano = Cano(cano)
    pontos = 0
    while sair is False:
        if int(pontos)%50 == 0:
            frames +=1
        pontos+=0.1
        cano.recriar()
        
        y-=velocidade_mapa
        x-=velocidade_mapa
        if x == -largura:
            
            x=largura
        if y == -largura:
            y = largura
        
        
        
        if jogador.rect.top < solo:
            vy += 1
        elif jogador.rect.top >= solo:
            vy = 0
            jogador.rect.top = solo
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and jogador.rect.top == solo:
                    uppress = True
                    vy = - velocidade
            

                           
        tela.blit(img_fundo1,(x,0))
        tela.blit(img_fundo2, (y,0))
        jogador.update(tela)
        jogador.mover(vx, vy)
        cano.update(tela)
        cano.mover()
        
        
        
        
        if colisao(jogador,cano):
            sair = True
            print(f'voce fez {int(pontos)} pontos')

        
        
        

        relogio.tick(frames)
        pygame.display.update()
    pygame.quit()                


main(frames)