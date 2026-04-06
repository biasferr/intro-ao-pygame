from pygame import *
import sys

init()

#importando imagem
cachorro_img= image.load("golden retriver.png")
cachorro_img = transform.scale(cachorro_img, (200,200))

cachorro_font= font.Font("Shelter Coffee.otf", 40)

#carregar musica
# mixer.music.load(#arquivo da minha musica)
# mixer.music.play(-1)

window = display.set_mode((1280,720))

#definir cor pro fundo
window.fill((151, 209, 250))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    #desenhar a partir daqui
    draw.rect(window,(72, 157, 37), (0,620,1280,100))
    draw.rect(window,(255,192,203), (320,360,270,260))
    draw.polygon(window, (94, 33, 41),((320,360),(455,170),(590,360)))
    draw.rect(window,(121, 77, 27), (455,440,80,180))

    #desenhar imagens
    window.blit(cachorro_img,(700,450))

    #desenhar texto
    cachorro_text= cachorro_font.render("Cuidado, cachorro bravo!", True, (0,0,0))
    window.blit(cachorro_text, (700,400))

    display.update()

