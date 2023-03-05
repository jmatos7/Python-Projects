import pygame

pygame.init()


janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('criando um jogo com python')

janela_aberta = True

x = 400
y = 300
pos_x = 200
pos_y = 300
velocidade = 10
personagem = pygame.image.load('images.png')
rua = pygame.image.load('rua.png')
flapy = pygame.image.load('flapy.png')

while janela_aberta :
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    
    if comandos[pygame.K_UP]:
       y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    if comandos[pygame.K_RIGHT]:
        x+= velocidade
    if comandos[pygame.K_LEFT]:
        x-= velocidade
    
    janela.blit(rua,(150,50))
    janela.blit(flapy,(pos_x,pos_y))
    janela.blit(personagem,(x,y))
    
    pygame.display.update()


pygame.quit()
