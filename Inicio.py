from Alinhamento import alinhar_rapido
from MovimentarTerra import segue_linha

from time import sleep

def achar_cor(bot, vel = 40.0, vazio=False):
    bot.mover.frente(vel)

    while bot.cores.cor('esq') == 6 and bot.cores.cor('dir') == 6: continue # Anda enquanto ver branco
    bot.mover.parar()

    if bot.cores.cor('esq') != 6: cor = bot.cores.cor('esq')
    else: cor = bot.cores.cor('dir')


    print(cor)
    if cor == 7 or cor == 6: achar_cor(bot, vel, vazio) #Aviso falso, procura novamente
    else:
        print("achou outra cor")
        bot.mover.parar() 
        sleep(0.5)
        alinhar_rapido(bot)
        if cor == 0:
            bot.mover.distancia(-20,25)
            bot.mover.girar(90,30)
            return achar_cor(bot)

        elif cor == 3: return

        else:
            print('caso 3')
            print(cor)
            bot.mover.distancia(dist=6,vel=20)
            bot.mover.girar(90,20)

            print("seguir linha")
            while segue_linha(bot,action="",vel = 30) != "vazio": sleep(0.05)

            print(bot.mapa)
            bot.mover.distancia(-20,30)
            bot.mover.girar(90,30)
            return achar_cor(bot)