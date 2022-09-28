#!/usr/bin/env python3
from Bot_Larc import Bot
import Buscar
from time import sleep
from math import pi

def alinhar(bot):
    while True:
        acha_vazio(bot)
        dir = re_vazio(bot)
        if dir == 0: return
        bot.mover.tras()
        sleep(1)
        bot.mover.parar()
        bot.mover.girar(dir*5)


def acha_vazio(bot):
    bot.mover.frente()
    while True:
        sleep(0.1)
        if bot.cor_dir.color == 0 or bot.cor_esq.color == 0:
            bot.mover.parar()
            return
            
        
def re_vazio(bot):
    bot.mover.tras(5)
    while True:
        sleep(0.2)
        if bot.cor_dir.color == 0 and bot.cor_esq.color == 0: continue
        elif bot.cor_dir.color == 0: return -1
        elif bot.cor_esq.color == 0: return 1
        else: return 0

if __name__== '__main__':
    bot = Bot()
    Buscar.segue_linha(bot)

    
    
