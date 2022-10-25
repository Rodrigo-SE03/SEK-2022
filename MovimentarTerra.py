from Seguidor import colorPID
from time import sleep, time

cores = [2,5,4]

def mapear(bot):
    cor = bot.cores.cor('esq')
    if cor not in [0,1,3,6] and cor not in bot.mapa:
        bot.mapa.append(cor)


def segue_linha(bot, action, side='dir',vel = 25):

    if side == 'esq':
        lado = colorPID(bot.cor_esq,vel) # pra ele seguir com o sensor esquerdo
        sensor_cor = 'dir'
        ajuste = -1

    else:
        lado = colorPID(bot.cor_dir,vel)
        sensor_cor = 'esq' 
        ajuste = 1
        
    if action == "take": mapear(bot)
    cor = bot.cores.cor(sensor_cor)
    
    cano = 0
    old = time()
    while bot.cores.cor(sensor_cor) == cor:
        print(bot.mede_dist('l'))
        print(bot.cores.cor(sensor_cor))
        if bot.cores.cor(sensor_cor) == 4: cano = 10
        elif bot.cores.cor(sensor_cor) == 5: cano = 15
        elif bot.cores.cor(sensor_cor) == 2: cano = 20

        correcao = lado.PID()*ajuste
        if abs(correcao) > 100: correcao = 100 * (correcao  / abs(correcao))
        bot.mover.steering_pair.on(correcao,lado.power)

        intervalo = time() - old
        if action == "take" and bot.pref == cano and intervalo >3.5: 
            dist = bot.mede_dist('l')
            if bot.mede_dist('l')<18: return  "pode_pegar"

        elif bot.cores.cor(sensor_cor) == 0: return "vazio"
    
    bot.mover.parar()
    if bot.cores.cor('esq') == 0 or bot.cores.cor('dir') == 0:  return  "vazio"
    else: 
        bot.mover.distancia(10)
        return "outra_cor"

def pegar_cano(bot):

    cor = bot.cores.cor('esq')
    dist = bot.mede_dist('l')

    if cor == 5: 
        cano = 15

    elif cor == 4: 
        cano = 10

    else: 
        cano = 20

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
    bot.garra.abrir()
    sleep(0.5)

    
    dist = size+8
    bot.mover.distancia(dist = -dist,vel = 10)
    sleep(0.5)
    bot.mover.distancia(1)

    bot.garra.subir()
    bot.garra.fechar()

    bot.set_cano(cano)
    bot.mover.distancia(dist)
    return