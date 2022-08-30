#!/usr/bin/env python3
from Bot_Larc import Bot

from time import sleep
from math import pi

if __name__== '__main__':
    bot = Bot()
    
    while True:
        bot.mover.girar(90)
        sleep(2)
        bot.mover.girar(-90)
        sleep(2)
        bot.mover.girar(-90)
        sleep(2)
        bot.mover.girar(-90)
        sleep(2)
        bot.mover.parar()