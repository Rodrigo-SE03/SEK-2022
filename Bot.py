#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_C, OUTPUT_D, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, InfraredSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound

from time import sleep
from math import pi
from cores import Cores

class Movimentos():
    vel_padrao = 10
    motor_esq = LargeMotor(OUTPUT_A)
    motor_dir = LargeMotor(OUTPUT_D)
    steering_pair = MoveSteering(OUTPUT_A,OUTPUT_D)
    
    def __init__(self):
        self.steering_pair = MoveSteering(OUTPUT_A,OUTPUT_D)

        distancia_entre_rodas = 19#    CALIBRAAAAR!!!!!!!!!!!!!!1
        raio_das_rodas = 1.5
        #self.giro_graus = (distancia_entre_rodas*pi)/(2*pi*raio_das_rodas)
        self.giro_graus = 6.3
        self.cano = 0
    
    def girar(self,graus,vel=vel_padrao, alinhar = False):
        dir = 1 #sentido anti-horario

        if self.cano == 0 or alinhar: correcao = 0
        elif self.cano == 10: correcao = 30
        elif self.cano == 15: correcao = 50
        else: correcao = 20
        if graus<0:
            dir = -1 #sentido horario
            graus = -graus
        self.steering_pair.on_for_degrees(100*dir,vel,graus*self.giro_graus - correcao)
        self.steering_pair.off()
    
    def frente(self,vel=vel_padrao,dir = 0): self.steering_pair.on(dir,vel)
    def tras(self,vel=vel_padrao): self.steering_pair.on(0,-vel)
    def parar(self): self.steering_pair.off()
    def distancia(self,dist,vel=vel_padrao):
        graus = dist*36
        self.steering_pair.on_for_degrees(0,vel,graus)

class Garra():
    vel_padrao = 10
    def __init__(self):
        self.motor = MediumMotor(OUTPUT_C)
        self.presa = MediumMotor(OUTPUT_B)
    
    def subir(self, vel = vel_padrao,grande = False):

        self.motor.on(vel)
        while True:
            sleep(0.1)
            # if grande: 
            #     self.motor.on(vel)
            #     print("tentando")
            if 'overloaded' in self.motor.state:  break

        self.motor.off()
            
    def descer(self, vel = vel_padrao): 
        self.motor.on(-vel) 
        while True:
            sleep(0.1)
            if 'overloaded' in self.motor.state:  break
        self.motor.off()

    def abrir(self, vel=vel_padrao):
        self.presa.on(vel) 
        while True:
            sleep(0.1)
            if 'overloaded' in self.presa.state:  break
        self.presa.off()
    
    def fechar(self, vel=vel_padrao):
        self.presa.on(-vel) 
        while True:
            sleep(0.1)
            if 'overloaded' in self.presa.state:  break
        self.presa.off()

class Bot():
    tamanho_cano = [10, 15, 20]
    som = Sound()

    mapa = []
    gasoduto = []
    pref = 0
    delta = 5.920097589492798/15 #tempo que o robo gasta para andar 1cm  - o numerador é obtido na calibracao
    size = 22

    dist_sensores =  10

    def __init__(self):
        self.cor_esq = ColorSensor(INPUT_3)
        self.cor_dir = ColorSensor(INPUT_2)

        self.lateral = InfraredSensor(INPUT_4)
        self.frontal = UltrasonicSensor(INPUT_1)

        self.cano = Cano()

        self.mover = Movimentos()
        self.garra = Garra()
        self.garra.descer()
        self.garra.abrir()

        self.cores = Cores([self.cor_dir, self.cor_esq])

        self.fator_calibracao_iv = 0.5
        self.turn = 0

        
    
    def mede_dist(self,sensor):
        if sensor == 'f':
            return self.frontal.distance_centimeters
        elif sensor == 'l':
            return self.lateral.proximity * self.fator_calibracao_iv #CALIBRAR FATOR NO DIA
        else: 
            raise Exception('Lmebre de definir qual sensor desejas saber a medida')
    
    def set_cano(self, cano):
        self.cano.tamanho = cano
        self.mover.cano = cano

    def get_cano(self):
        return self.cano.tamanho
    
    def btn(self):
        return Button()


    def ir_cor(self,cor,vel = 25):
        self.mover.frente(vel)
        while self.cores.cor('esq') != cor and self.cores.cor('dir') != cor: continue
        self.mover.parar()
    
    def ir_dist(self,dist,vel = 25):
        self.mover.frente(vel)
        while self.mede_dist('f') > dist: 
            continue
        self.mover.parar()

    def finalizar(self):
        while True:
            sleep(0.5)
            self.garra.subir()
            sleep(0.5)
            self.garra.descer()
    
    def reset_list(self):
        self.cano.list_espacos = []
    
    def add_espaco(self, size):
        self.cano.list_espacos.append(size)

class Cano():
    def __init__(self):
        self.colocado = False
        self.devolvido = False
        self.tamanho = 0
        self.espaco = 0
        self.list_espacos = []
        self.comp = 0


if __name__== '__main__':
    bot = Bot()
    bot.mover.tras()
    sleep(4)
    bot.mover.girar(90)
