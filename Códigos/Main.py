#!/usr/bin/env python3
from Bot import Bot

from time import sleep
from math import pi

if __name__== '__main__':
    print("here")
    bot = Bot()

    while True:
        bot.mover.frente()
        sleep(2)
        bot.mover.girar(90)
        sleep(2)
        bot.mover.girar(-180)
        sleep(2)
        bot.mover.girar(90)
        sleep(2)
        bot.mover.tras()
        sleep(2)
        bot.mover.parar()