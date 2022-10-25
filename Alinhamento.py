#!/usr/bin/env python3

def alinhar_rapido(bot):
    bot.mover.distancia(1)
    while bot.cores.cor('esq') !=6 or bot.cores.cor('dir') !=6:
        print('esq: {}'.format(bot.cores.cor('esq')))
        print('dir: {}'.format(bot.cores.cor('dir')))
        if bot.cores.cor('esq') !=6:
            print('esq')
            bot.mover.motor_esq.on_for_degrees(30,-20)
        if bot.cores.cor('dir') !=6:
            print('dir')
            bot.mover.motor_dir.on_for_degrees(30,-20)
    bot.mover.parar()