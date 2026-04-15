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
cor_manha = (151,209,250)
cor_tarde = (255, 177, 94)
cor_noite = (39, 17, 145)
background_color = (151,209,250)



audio_manha = mixer.Sound ("manhã.mp3")
audio_tarde = mixer.Sound ("tarde.mp3")
audio_noite = mixer.Sound ("noite.mp3")
estado = 'teclado'

while True:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        if ev.type == MOUSEBUTTONUP:
            if ev.button == 1:
                #mudança de audio
                
                if estagio == 'manhã':
                    audio_manha.play()
                    
                elif estagio == 'tarde':
                    audio_tarde.play()
                    
                elif estagio == 'noite':
                    audio_noite.play()
                    
        if ev.type == KEYDOWN:
            if ev.key == K_m:
                if estado == 'mouse':
                    estado = 'teclado'  
                elif estado == 'teclado':
                    estado = 'mouse'         
            
    

    ##movimentos
    dt= clock.get_time()/1000
    keys= key.get_pressed()
    # mousee = mouse.get_pressed()
        #movimento sol
    
    if estado == 'teclado': 
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
    elif estado == 'mouse':
        sol_x, sol_y = mouse.get_pos()
        
    
    #mudança de cor do céu
    if sol_y < 350:
        background_color = cor_manha
        estagio = 'manhã'
    elif sol_y < 650:
        background_color = cor_tarde
        estagio = 'tarde'
    else:
        background_color = cor_noite 
        estagio = 'noite'

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

