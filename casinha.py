from pygame import *
import sys

init()

#importando imagem
cachorro_img= image.load("golden retriver.png")
cachorro_img = transform.scale(cachorro_img, (200,200))

cachorro_font= font.Font("Shelter Coffee.otf", 40)

#carregar musica
mixer.music.load("still-into-you.mp3")
mixer.music.play(-1)


window = display.set_mode((1280,720))
running = True
clock= time.Clock()

#definir cor pro fundo
window.fill((151, 209, 250))


#definir variáveis
nuvem_x= 750
nuvem_y= 125
velocidade_nuvem= 100
background_color= (151, 209, 250)

while True:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        if ev.type == KEYDOWN:
            tecla = ev.key
            if background_color == (151,209,250):
                if tecla == K_SPACE:
                    background_color = (255, 177, 94)
            elif background_color == (255, 177, 94):
                if tecla == K_SPACE:
                    background_color == (39, 17, 145)
            elif background_color == (39, 17, 145):
                if tecla == K_SPACE:
                    background_color = (151,209,250)
            


    window.fill(background_color)

    ##movimentos
    dt= clock.get_time()/1000
    keys= key.get_pressed()

   
    # if keys[K_RIGHT]:
    #     nuvem_x = nuvem_x + velocidade_nuvem * dt
    # elif keys[K_LEFT]:
    #     nuvem_x= nuvem_x - velocidade_nuvem * dt
    
    #movimento da nuvem
    nuvem_x_ida = nuvem_x + velocidade_nuvem * dt
    nuvem_x_volta = - (nuvem_x + velocidade_nuvem * dt)
    if nuvem_x > 1050:
        nuvem_x_volta

    elif nuvem_x <50:
        nuvem_x= 50
    
    
    ##desenhos
    #desenhando casa
    draw.rect(window,(72, 157, 37), (0,620,1280,100))
    draw.rect(window,(255,192,203), (320,360,270,260))
    draw.polygon(window, (94, 33, 41),((320,360),(455,170),(590,360)))
    draw.rect(window,(121, 77, 27), (455,440,80,180))
    draw.rect(window,(13, 23, 100), (353,480,67,100))
    draw.circle(window,(0,0,0),(470,530),6)

    #desenhando arvore
    draw.rect(window, (120, 77, 26), (960,360,55,260))
    draw.circle(window,(71, 156, 37),(987,400), 100)

    #desenhar sol
    draw.circle(window, (255,222,33), (150,125),(50))
    draw.line(window,(255,222,33),(150,230), (150,20),(7))
    draw.line(window,(255,222,33), (40,125), (260,125),(7))
    draw.line(window, (255,222,33),(60,50), (220,200),(7))
    draw.line(window, (255,222,33),(220,50), (60,200),(7))

    #desenhar nuvem
    draw.circle(window,(255,255,255),(nuvem_x,nuvem_y),50)
    draw.circle(window,(255,255,255),(nuvem_x + 60,nuvem_y),50)
    draw.circle(window,(255,255,255),(nuvem_x + 120,nuvem_y),50)
    draw.circle(window,(255,255,255),(nuvem_x + 180,nuvem_y),50)

    #desenhar imagens
    window.blit(cachorro_img,(700,450))

    #desenhar texto
    cachorro_text= cachorro_font.render("Cuidado, cachorro bravo!", True, (0,0,0))
    window.blit(cachorro_text, (700,400))

    display.update()

