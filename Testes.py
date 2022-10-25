#!/usr/bin/env python3
from Bot import Bot
from Alinhamento import *
from Calibrar import *
from Inicio import achar_cor
from MovimentarGasoduto import *
from MovimentarTerra import *
from Main import *


def teste_pegar(tamanho): #começa com o robô sobre a fita olhando no sentido negativo
    bot.set_cano(tamanho) #define qual cano vai tentar pegar - para só seguir a linha, basta usar cano = 0
    pegar(bot)
    print(bot.mapa)

def teste_ver_espaco(bot): #começa com o robô virado pro verde 
    ir_pro_gasoduto(bot)
    alinhar_gasoduto(bot)
    ir_inicio(bot)
    alinhar_gasoduto(bot)
    bot.mover.girar(90)
    act = move_gasoduto(bot)
    print(act)
    print(bot.cano.espaco)
    print(bot.cano.list_espacos)

def teste_colocar(bot): #começa com o robô de frente pro gasoduto pra alinhar
    alinhar_gasoduto(bot)
    bot.mover.girar(90)
    move_gasoduto(bot)
    colocar(bot)

def teste_devolver():
    target = bot.mapa.index(cano_cor(bot.cano.tamanho))
    voltar(bot, vel=25, giro=50)
    pos = bot.cores.cor("dir")

    devolver(pos)
    
    bot.mover.parar()

def teste_levantar(bot):
    ajuste = 12
    bot.mover.tras(10)
    while bot.mede_dist('l') < 35*bot.fator_calibracao_iv:
        print(bot.mede_dist('l'))
        continue
    bot.mover.distancia(dist = 5) 
    sleep(0.5)
    dist = bot.mede_dist('l')

    bot.mover.girar(90) 
    sleep(0.5)
    
    comp = dist+10
    bot.mover.distancia(dist = -comp,vel = 20)
    sleep(0.5)
    bot.mover.distancia(1)

    bot.garra.fechar()
    bot.garra.subir()
    
def pegar_comprimento(bot):
    bot.mover.tras(10)
    while bot.mede_dist('l') < 35*bot.fator_calibracao_iv:
        print(bot.mede_dist('l'))
        continue
    bot.mover.parar()
    bot.mover.distancia(1)
    old = time()
    bot.mover.frente()
    while bot.mede_dist('l') < 35*bot.fator_calibracao_iv:
        continue
    bot.mover.parar()
    intervalo = time() - old
    comp = intervalo/bot.delta
    bot.mover.distancia(-comp)
    size = bot.mede_dist('l')

    bot.mover.girar(90) 
    sleep(0.5)

    
    dist = size+8
    bot.mover.distancia(dist = -dist,vel = 10)
    sleep(0.5)
    bot.mover.distancia(1)

    bot.garra.fechar()
    bot.garra.subir()

    bot.mover.distancia(dist)
    return
    

def abre_fecha(bot):
    while True:
        bot.garra.abrir()
        print('abriu')
        sleep(1)
        bot.garra.fechar()
        print('fechou')
        sleep(1)

def girar_calibracao(bot,cano = 0,vel = 10):
    bot.cano = cano
    while True:
        bot.mover.girar(90,vel)
        sleep(2)


if __name__== '__main__':
    bot = Bot()

    # girar_calibracao(bot)

    wait_btn(bot)
    bot.pref = 10
    teste_pegar(10)
    # bot.garra.subir()
    # bot.garra.motor.on_for_degrees(10, -45)
    # mede_espaco(bot)
    
    # while True:
    #     bot.garra.subir()
    #     bot.garra.fechar()
    #     print("subiu")
    #     sleep(5)
    #     bot.mover.girar(-5)
    #     bot.mover.girar(10)
    #     bot.garra.abrir()
    #     bot.garra.descer()
    #     print("desceu")
    #     sleep(5)

    # bot.garra.subir()
    # bot.garra.motor.on_for_degrees(10, -45)
    # bot.garra.fechar()
    # bot.mover.distancia(5)
