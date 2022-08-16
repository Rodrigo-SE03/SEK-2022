#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_D
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
        distancia_entre_rodas = 18
        raio_das_rodas = 1.75
        self.giro_graus = (distancia_entre_rodas*pi)/(2*pi*raio_das_rodas)

    def girar(self,graus,vel=vel_padrao):
        dir = 1
        if graus<0:
            dir = -1
            graus = -graus
        self.steering_pair.on_for_degrees(100*dir,vel,graus*self.giro_graus)
        self.steering_pair.off()
    
    def frente(self,vel=vel_padrao): self.steering_pair.on(0,vel)
    def tras(self,vel=vel_padrao): self.steering_pair.on(0,-vel)
    def parar(self): self.steering_pair.off()

class Bot():
    def __init__(self):
        self.cor_esq = ColorSensor(INPUT_2)
        self.cor_dir = ColorSensor(INPUT_3)

        #self.ultsnc_lado = UltrasonicSensor(INPUT_1)
        #self.ultsnc_frente = UltrasonicSensor(INPUT_4)

        self.mover = Movimentos()
