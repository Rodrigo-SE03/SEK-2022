#!/usr/bin/env python3
from Bot import Bot
from Alinhamento import *
from Calibrar import *
from Inicio import achar_cor
from MovimentarGasoduto import *
from MovimentarTerra import *
import logging

logging.basicConfig(filename='main.log', level=logging.DEBUG)

'''
0: No color
1: Black
2: Blue
3: Green
4: Yellow
5: Red
6: White
# 7: Brown
'''

def pegar(bot):
    while segue_linha(bot, action=" ", side='esq') != "vazio": sleep(0.05)
        
    bot.mover.distancia(-10, 20)
    bot.mover.girar(180, 20)
    while bot.cores.cor('dir') != 6: 
        bot.mover.girar(20)
    bot.mover.girar(20)
    bot.mover.parar()
    while segue_linha(bot, action="take") != "pode_pegar": sleep(0.05)
    pegar_cano(bot)

    bot.mover.girar(-90)
    while segue_linha(bot, action=" ") != "vazio": sleep(0.5)
    bot.mover.distancia(-20,20)
    bot.mover.girar(90)
    bot.mover.distancia(10,20)
    return

def colocar(bot):
    bot.garra.abrir()
    bot.garra.subir()
    # bot.mover.girar(-90,20)   #TESTAR
    # alinhar_gasoduto(bot)
    bot.mover.distancia(-bot.cano.comp+3)
    bot.mover.girar(90,20)
    bot.mover.distancia(-15,10)

    sleep(1)
    bot.garra.motor.on_for_degrees(25,-90)
    bot.garra.abrir()
    bot.set_cano(0)
    try:
        bot.cano.list_espacos.remove(bot.cano.tamanho)
    except:
        pass
    sleep(2)
    
    bot.mover.distancia(10,20)
    bot.mover.parar()
    bot.garra.descer()
    bot.mover.girar(-90,40)

    bot.cano.colocado = True
    return

def devolver(pos):
    if target > pos: 
        bot.mover.girar(180, 20)
        while  bot.cores.cor("esq") != target: segue_linha(bot, action="")
        bot.mover.distancia(15, 25)
        bot.mover.girar(90)
        bot.mover.distancia(-15, 10)
        bot.garra.descer()
        bot.set_cano(0)
        bot.cano.list_espacos.remove(bot.cano.tamanho)
        

        bot.ir_cor(6, 30)
        bot.mover.distancia(10, 20)
        bot.cano.devolvido = True
        if  len(bot.cano.list_espacos) == 0: bot.finalizar()

    elif target == pos: 
        bot.mover.girar(180, 50)
        while  bot.cores.cor("esq") == target: segue_linha(bot, action="")
        bot.mover.distancia(-10, 25)
        bot.mover.girar(90)
        bot.mover.distancia(-15, 10)
        bot.garra.descer()
        bot.set_cano(0)
        bot.cano.list_espacos.remove(bot.cano.tamanho)
        

        bot.ir_cor(6, 30)
        bot.mover.distancia(10, 30)
        bot.cano.devolvido = True
        if  len(bot.cano.list_espacos) == 0: bot.finalizar()
    else: #target < len
        while  bot.cores.cor("dir") != target: segue_linha(bot, action="", side='esq')
        bot.mover.distancia(15, 25)
        bot.mover.girar(90)
        bot.mover.distancia(-15, 10)
        bot.garra.descer()
        bot.set_cano(0)
        bot.cano.list_espacos.remove(bot.cano.tamanho)

def cano_cor(size):
    if size == 10: return 4
    elif size == 15: return 5
    else: return 2

if __name__== '__main__':
    bot = Bot()
    inicio = True
    

#   wait_btn(bot)

    while True:
        if bot.cano.devolvido and len(bot.cano.list_espacos) != 0:
            bot.mover.girar(-90, 20)
            pegar(bot)
            bot.cano.devolvido = False
            continue
       
        elif not bot.cano.colocado:
            
            achar_cor(bot)

            '''gasoduto'''
            if inicio:
                ir_pro_gasoduto(bot,60)
            else:
                ir_pro_gasoduto(bot) 
            alinhar_gasoduto(bot)

            if inicio:
                ir_inicio(bot,50)
            else:
                ir_inicio(bot)
        
        bot.cano.colocado = False
        bot.cano.devolvido = False
        if len(bot.cano.list_espacos) == 0:  
            print('here')
            act = move_gasoduto(bot)
        else: act = "pegar"

        if act == "Pegar":
            bot.pref = bot.cano.list_espacos[0]
            bot.garra.descer()
            voltar(bot)
            pegar(bot)
        elif act == "Colocar": 
            colocar(bot)
        elif act == "Devolver": 
            
            target = bot.mapa.index(cano_cor(bot.cano.tamanho))
            voltar(bot, vel=25, giro=20)
            pos = bot.cores.cor("dir")

            devolver(pos)


            while segue_linha(bot, action=" ") != "vazio": sleep(0.5)  #perguntar pro pp
                
            bot.mover.distancia(-5, 20)
            bot.mover.girar(180, 30)
            while segue_linha(bot, action="take") != "pode_pegar": sleep(0.5)
            pegar_cano(bot)

            bot.mover.girar(-90, 30)
            while segue_linha(bot, action=" ") != "vazio": sleep(0.5)
            bot.mover.distancia(-10, 20)
            bot.mover.girar(90, 20)
            bot.mover.distancia(10, 20)
        
        inicio = False