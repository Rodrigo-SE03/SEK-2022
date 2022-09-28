#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MediumMotor, OUTPUT_A, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor

from time import sleep
from math import pi

class Movimentos():
    vel_padrao = 10
    def __init__(self):
        self.steering_pair = MoveSteering(OUTPUT_A,OUTPUT_D)

        distancia_dos_motores = 12.5
        raio_engrenagem = 2.5
        distancia_entre_rodas = 25
        raio_das_rodas = 1.75
        self.giro_graus = (distancia_entre_rodas*pi)/(2*pi*raio_das_rodas)
    
    def girar(self,graus,vel=vel_padrao):
        dir = 1 #sentido anti-horario
        if graus<0:
            dir = -1 #sentido horario
            graus = -graus
        self.steering_pair.on_for_degrees(100*dir,vel,graus*self.giro_graus)
        self.steering_pair.off()
    
    def frente(self,vel=vel_padrao): self.steering_pair.on(0,vel)
    def tras(self,vel=vel_padrao): self.steering_pair.on(0,-vel)
    def parar(self): self.steering_pair.off()
    def distancia(self,dist,vel=vel_padrao):
        dist = dist+1
        graus = dist*35
        self.steering_pair.on_for_degrees(0,vel,graus)
        

class Garra():
    vel_padrao = 10
    def __init__(self):
        self.motor = MediumMotor(OUTPUT_C)
    
    def subir(self, vel = vel_padrao): 
        self.motor.on(vel) 
        while True:
            sleep(0.1)
            if 'overloaded' in self.motor.state:  break
        self.motor.off
    def descer(self, vel = vel_padrao): 
        self.motor.on(-vel) 
        while True:
            sleep(0.1)
            if 'overloaded' in self.motor.state:  break
        self.motor.off

class Bot():
    def __init__(self):
        self.cor_esq = ColorSensor(INPUT_2)
        self.cor_dir = ColorSensor(INPUT_3)

        self.ultsnc_lado = UltrasonicSensor(INPUT_4)
        self.ultsnc_frente = UltrasonicSensor(INPUT_1)

        self.mover = Movimentos()
        self.garra = Garra()
        self.garra.descer()
    
    def mede_dist(self,sensor):
        if sensor == 'f':
            return self.ultsnc_frente.distance_centimeters
        else:
            return self.ultsnc_lado.distance_centimeters

 class Alinhamento():
    def __init__(self, bot): 
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
        else: 
            return 0
