from time import sleep, time
from ev3dev2.sound import Sound

sprk = Sound()

def wait_btn(bot):
    print("pressione um botao")
    sprk.beep()
    while True:
        if bot.btn().any(): 
            print("valeu chefia")
            return
        else: sleep(0.01)

def girar_calibracao(bot,cano = 0,vel = 10):
    bot.cano = cano
    while True:
        bot.mover.girar(90,vel)
        sleep(2)
    
def dist_calibracao(bot):
    old = time()
    bot.mover.distancia(5,vel = 10)
    new = time()
    return (new - old)

def dist_calibracao_2(bot):
    bot.mover.tras()
    while bot.mede_dist('l') < 10:
        continue
    bot.mover.parar()
    bot.mover.distancia(1)
    old = time()
    bot.mover.frente()
    print('start')
    while bot.mede_dist('l') < 10:
        continue
    print('end')
    print(time() - old)
    bot.mover.parar()
    

def girar_calibracao_2(bot):
    resolucao = 5
    cont = 0
    while bot.mede_dist('f') > 5:
        print( bot.mede_dist('f'))
        bot.mover.steering_pair.on_for_degrees(100,10,resolucao)
        cont += resolucao
    bot.mover.parar()
    print(cont)
    print(cont/180)
  

def calibrar_cor(bot):
    print("Aperte algum botao pls")
    wait_btn(bot)
    print("thanks")
    bot.mover.frente(10)

    cor_hsv = [[],[]]
    s = [[],[]]
    v = [[],[]]
    total = 10
    for i in range(total):
        cor_hsv[0].append(bot.cores.get_hsv('dir')[0])
        cor_hsv[1].append(bot.cores.get_hsv('esq')[0])
        s[0].append(bot.cores.get_hsv('dir')[1])
        s[1].append(bot.cores.get_hsv('esq')[1])
        v[0].append(bot.cores.get_hsv('dir')[2])
        v[1].append(bot.cores.get_hsv('esq')[2])
        perc = str((i/total)*100) + "%"
        print(perc)
        sleep(1)

    bot.mover.parar()
    cor_hsv_max_dir =  max(cor_hsv[0])
    cor_hsv_min_dir =  min(cor_hsv[0])
    cor_hsv_max_esq =  max(cor_hsv[1])
    cor_hsv_min_esq =  min(cor_hsv[1])

    s_max_dir = max(s[0])
    s_min_dir = max(s[0])
    s_max_esq = max(s[1])
    s_min_esq = max(s[1])

    v_max_dir = max(v[0])
    v_min_dir = max(v[0])
    v_max_esq = max(v[1])
    v_min_esq = max(v[1])


    print("! ")
    print("dir: H")
    print(cor_hsv_max_dir)
    print(cor_hsv_min_dir)
    print("S")
    print(s_max_dir)
    print(s_min_dir)
    print("V")
    print(v_max_dir)
    print(v_min_dir)
    
    print("esq: H")
    print(cor_hsv_max_esq)
    print(cor_hsv_min_esq)
    print("S")
    print(s_max_esq)
    print(s_min_esq)
    print("V")
    print(v_max_esq)
    print(v_min_esq)