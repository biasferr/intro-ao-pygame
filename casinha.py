from pygame import *
import sys

init()

#importando imagem
cachorro_img= image.load("golden retriver.png")
cachorro_img = transform.scale(cachorro_img, (200,200))

cachorro_font= font.Font("Shelter Coffee.otf", 40)

#carregar musica

#audio_tarde = mixer.music.load("still-into-you.mp3")
#mixer.music.play(-1)


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
sol_x= 150
sol_y= 125
velocidade_sol = 200
manha = (151,209,250)
tarde = (255, 177, 94)
noite = (39, 17, 145)
background_color = (151,209,250)
estagio = 'manhã'



while True:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        if ev.type == MOUSEBUTTONUP:
            if ev.button == 1:
                if estagio == 'manhã':
                    mixer.music.load ("manhã.mp3")
                    mixer.music.play(-1)
                    estagio = 'tarde'
                elif estagio == 'tarde':
                    mixer.music.load ("tarde.mp3")
                    mixer.music.play(-1)
                    estagio = 'noite'
                elif estagio == 'noite':
                    mixer.music.load ("noite.mp3")
                    mixer.music.play (-1)
                    estagio = 'manhã'

        # if ev.type == KEYDOWN:
        #     tecla = ev.key
        #     if background_color == (151,209,250):
        #         if tecla == K_SPACE:
        #             background_color = (255, 177, 94)
        #     elif background_color == (255, 177, 94):
        #         if tecla == K_SPACE:
        #             background_color == (39, 17, 145)
        #     elif background_color == (39, 17, 145):
        #         if tecla == K_SPACE:
        #             background_color = (151,209,250)
            
    

    ##movimentos
    dt= clock.get_time()/1000
    keys= key.get_pressed()
    mousee = mouse.get_pressed()

    # mudança de audio
    

    #movimento sol
    if keys[K_RIGHT]:
        if sol_x >= 1175:
            sol_x= 1175
        else: 
            sol_x = sol_x + velocidade_sol * dt
    elif keys[K_LEFT]:
        if sol_x <= 100:
            sol_x = 100
        else:
            sol_x= sol_x - velocidade_sol * dt
    elif keys[K_UP]:
        if sol_y <= 105:
            sol_y= 105
        else:
            sol_y= sol_y - velocidade_sol * dt
    elif keys[K_DOWN]:
        if sol_y >= 740:
            sol_y= 740
        else:
            sol_y= sol_y + velocidade_sol * dt
    
    #mudança de cor do céu
    if sol_y < 350:
        background_color = manha
    elif sol_y < 650:
        background_color = tarde
    else:
        background_color = noite 

    #movimento da nuvem
    nuvem_x = nuvem_x + velocidade_nuvem * dt 
    if nuvem_x >= 1050:
        velocidade_nuvem = velocidade_nuvem * (-1)
    elif nuvem_x <= 50:
        velocidade_nuvem = velocidade_nuvem * (-1)

    
    
    ##desenhos    
    window.fill(background_color)

    #desenhar sol
    draw.circle(window, (255,222,33), (sol_x,sol_y),(50))
    draw.line(window,(255,222,33),(sol_x,sol_y + 105), (sol_x,sol_y - 105),(7))
    draw.line(window,(255,222,33), (sol_x - 90,sol_y), (sol_x + 110,sol_y),(7))
    draw.line(window, (255,222,33),(sol_x - 90, sol_y - 75), (sol_x + 70,sol_y + 75),(7))
    draw.line(window, (255,222,33),(sol_x + 70, sol_y - 75), (sol_x - 90,sol_y + 75),(7))


    #desenhar nuvem
    draw.circle(window,(255,255,255),(nuvem_x,nuvem_y),50)
    draw.circle(window,(255,255,255),(nuvem_x + 60,nuvem_y),50)
    draw.circle(window,(255,255,255),(nuvem_x + 120,nuvem_y),50)
    draw.circle(window,(255,255,255),(nuvem_x + 180,nuvem_y),50)


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

    



    #desenhar imagens
    window.blit(cachorro_img,(700,450))

    #desenhar texto
    cachorro_text= cachorro_font.render("Cuidado, cachorro bravo!", True, (0,0,0))
    window.blit(cachorro_text, (700,400))

    display.update()

