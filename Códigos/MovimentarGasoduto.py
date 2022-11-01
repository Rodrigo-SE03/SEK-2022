from time import sleep,time
from Alinhamento import  alinhar_rapido

def ir_inicio(bot,vel = 25):
    bot.mover.girar(-90)
    bot.ir_cor(0,vel)
    bot.mover.distancia(-10)
    bot.mover.girar(90)
    alinhar_gasoduto(bot)
    bot.mover.girar(90)
    return

def ir_pro_gasoduto(bot,vel = 25):
    print("indo pro gasoduto")
    bot.reset_list()
    bot.mover.frente(vel)
    while bot.cores.cor('esq') != 3 and bot.cores.cor('esq') !=3: continue
    alinhar_rapido(bot)
    bot.ir_dist(10,vel)
    return

def alinhar_gasoduto(bot, vel = 20):
    dist = bot.mede_dist('f')
    bot.mover.distancia(dist+25,vel)
    bot.mover.distancia(-5,20)
    return

def move_gasoduto(bot):

    bot.garra.abrir()
    bot.garra.subir()
    bot.garra.motor.on_for_degrees(10, -45)
    bot.garra.fechar()
    bot.turn = 0
    
    while bot.cores.cor('esq') != 0 and bot.cores.cor('dir') != 0:
        bot.mover.frente(vel = 30)
        if bot.mede_dist('l') > 15:
            sleep(0.5)
            bot.mover.parar()
            bot.garra.abrir()
            bot.garra.descer()
            bot.garra.motor.on_for_degrees(10, 80)
            bot.mover.distancia(5)
            bot.mover.distancia(-2)
            print(bot.mede_dist('f') )
            sleep(0.5)
            if bot.mede_dist('f') < 8:
                print('virar')
                pass
            elif bot.mede_dist('l') < 15:
                
                print('espaco detectado')

                bot.garra.abrir()
                bot.garra.subir()
                bot.garra.motor.on_for_degrees(10, -45)
                bot.garra.fechar()
                bot.mover.girar(-90,20)
                alinhar_gasoduto(bot)
                bot.mover.girar(90,20)

                espaco = mede_espaco(bot)
                if espaco == 0: 
                    continue
                else: 
                    if bot.cano.tamanho == 0: return "Pegar"
                    elif bot.cano.tamanho == bot.cano.espaco: return "Colocar"
            
            else: 
                print('curva para a esquerda')
                bot.garra.abrir()
                bot.garra.subir()
                bot.garra.motor.on_for_degrees(20, -45)
                bot.garra.fechar()
                bot.turn -= 1
                bot.mover.girar(-90,20)
                bot.mover.frente(20)
                while bot.mede_dist('l') > 15:
                    continue
                bot.mover.parar()
                bot.mover.distancia(15)
                bot.mover.girar(-90,20)
                alinhar_gasoduto(bot)
                bot.mover.girar(90,20)
            
            
            # else:
            #     bot.mover.girar(-90,20)
            #     alinhar_gasoduto(bot)
            #     bot.mover.girar(90,20)
            
               
                # elif espaco > 20:
                #     bot.bot.mover.distancia(5, 10)
                #     bot.mover.girar(-90)
                #     bot.mover.frente(vel = 30,dir = -0.5)
                
            
                    

        elif bot.mede_dist('f') < 8: 
            print('curva para a direita')
            bot.turn += 1
            alinhar_gasoduto(bot)
            bot.mover.girar(90)
            bot.garra.abrir()
            bot.garra.subir()
            bot.garra.motor.on_for_degrees(10, -45)
            bot.garra.fechar()
 
    bot.mover.parar()
    
    print ('Fim da pista')
    if bot.cano.tamanho != 0: return "Devolver"
    else: bot.finalizar()
   

def sons(som, qtd):
    for i in range(qtd): 
        som.beep()
        sleep(0.5)

def mede_espaco(bot):
    
    bot.mover.distancia(-2)
    bot.mover.tras()
    
    while bot.mede_dist('l') > 15: continue
    bot.mover.parar()

    old = time()
    
    bot.mover.frente()
    sleep(0.5)
    while bot.mede_dist('l') > 15:
        continue
    bot.mover.parar()
   
    intervalo = time() - old
    comp = intervalo/bot.delta
    bot.cano.comp = comp
    print(comp)
    print(intervalo)

    if comp < (bot.tamanho_cano[0]-5): return 0

    elif comp > (bot.tamanho_cano[0]-5) and comp <= (bot.tamanho_cano[0]):
        bot.cano.espaco = 10
        bot.add_espaco(10)
        sons(bot.som, 1)
       
    
    elif comp > (bot.tamanho_cano[0]) and comp <= (bot.tamanho_cano[1]):
        bot.cano.espaco = 15
        bot.add_espaco(15)
        sons(bot.som, 2)

    elif comp > (bot.tamanho_cano[1]) :
        bot.cano.espaco = 20
        bot.add_espaco(20)
        sons(bot.som, 3)

    else:
        bot.cano.espaco = 0
        return 25
    print(bot.cano.espaco)
    return bot.cano.espaco


def voltar(bot, vel = 30, giro = 30):

    bot.mover.girar(-90,20)
    alinhar_gasoduto(bot)

    if bot.turn == 0:
        bot.mover.girar(180, giro)
    elif bot.turn == 1:
        bot.mover.girar(90, giro)
    else:
        bot.mover.girar(-90, giro)
    bot.mover.frente(vel)
    bot.ir_cor(3, vel)

    bot.mover.distancia(80, vel)
    bot.mover.frente(20)
    while bot.cores.cor('esq') == 6 or bot.cores.cor('dir') == 6: continue
    bot.mover.parar()

    alinhar_rapido(bot)
    bot.mover.distancia(5)
    bot.mover.girar(-90)
    if bot.cores.cor('esq') == 6:
        while bot.cores.cor('esq') != 1:
            print('aqui')
            bot.mover.girar(10)
        bot.mover.girar(-15)
        
    elif bot.cores.cor('esq') != 1:
        while bot.cores.cor('esq') != 6:
            bot.mover.girar(-10)
            print('debaixo')
        bot.mover.girar(15)
    bot.mover.parar()