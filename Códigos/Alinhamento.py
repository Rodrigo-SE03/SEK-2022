#!/usr/bin/env python3
from Bot_Larc import Bot

from time import sleep


def alinha_vazio(Bot,lado):
    alinhando = True
    bot = Bot()
    while(alinhando):
        bot.mover.parar()
        if(lado == 1):
            sensor = bot.cor_esq
        else:
            sensor = bot.cor_dir
        while(sensor.color() != 0):
            bot.mover.girar(10)
        bot.mover.tras(15)
        sleep(2)
        bot.mover.frente()
        while bot.cor_esq != 0 or bot.cor_dir !=0:
            delay(0.1)
        bot.mover.parar()
        if bot.cor_esq == 0 and bot.cor_dir != 0:
            alinha_vazio(bot,1)
        elif bot.cor_dir == 0 and bot.cor_esq != 0:
            alinha_vazio(bot,2)
        elif bot.cor_esq == 0 and bot.cor_dir == 0:
            break
        
