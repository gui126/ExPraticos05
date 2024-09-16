import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Dimensãesda tela
largura = 600
altura  = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo da cobrinha')

 # Definindo cores
azul = (0, 0, 255)
vermelho= (255, 0, 0)
preto = (0, 0, 0)

# comfiguração de jogo
tamanho_celula = 20
velocidade = 5
relogio = pygame.time.Clock()



# Função para gerar a comida  em posição aleatória
def gera_comida():
    x_comida = random.randrange(0, largura, tamanho_celula)
    y_comida = random.randrange(0, altura, tamanho_celula)
    return x_comida, y_comida

# função para desenhar acobrinha
def desenhar_cobrinha(cobra):
    for parte in cobra:
        pygame.draw.rect(tela, azul, (parte[0], parte[1], tamanho_celula, tamanho_celula))

# função principal
def jogo():
    x = largura // 2
    y = altura // 2
    x_velocidade = 0
    y_velocidade = 0
    cobra = [(x, y)]
    comprimento_cobra = 1

    x_comida, y_comida = gera_comida()

    while True:
        # detecta eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # catura as teclas para movar a cobrinha
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_velocidade == 0:
                    x_velocidade = -tamanho_celula
                    y_velocidade =0
                elif evento.key == pygame.K_RIGHT and x_velocidade == 0:
                    x_velocidade = -tamanho_celula
                    y_velocidade = 0
                elif evento.key == pygame.K_UP and y_velocidade == 0:
                    y_velocidade = - tamanho_celula
                    x_velocidade = 0
                elif evento.key == pygame.K_DOWN and y_velocidade == 0:
                    y_velocidade = tamanho_celula
                    x_velocidade = 0

        # atualiza a posição da cobrinha
        x += x_velocidade
        y += y_velocidade
        cobra.append((x,y))

        #mantem o tamanho da cobrinha
        if len(cobra) > comprimento_cobra:
            del cobra[0]
        # detecta colisão com as bordas ou com o proprio corpo
        if x < 0 or x >= largura or y < 0 or y >= altura or (x, y) in cobra[:-1]:
            break
    
        # detecta se a cobrilha comeu a comida
        tela.fill(preto)
        desenhar_cobrinha(cobra)
        pygame.draw.rect(tela, vermelho, (x_comida, y_comida, tamanho_celula, tamanho_celula))
        pygame.display.flip()

        relogio.tick(velocidade)

# inicia o jogo
jogo()