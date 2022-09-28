from Seguidor import colorPID
from time import sleep


def segue_linha(bot):
    direita = colorPID(bot.cor_dir)
    esquerda = colorPID(bot.cor_esq)
    
    while True:
        correcao = -direita.PID()
        if abs(correcao) > 100: correcao = 100 * (correcao  / abs(correcao))
        bot.mover.steering_pair.on(correcao,colorPID.power)
        dist = bot.mede_dist('l')
        print(dist)
        if dist < 30:
            break
    
    bot.mover.distancia(dist = 7.5-2) #Esse 7.5 é metade do tamanho do cano de 15cm. A ideia é trocar esse valor por uma variável "tamanho" de acordo com a cor abaixo do robô
    sleep(0.5)
    bot.mover.girar(90)
    sleep(0.5)
    bot.mover.distancia(dist = -dist)
    sleep(0.5)
    bot.garra.subir()