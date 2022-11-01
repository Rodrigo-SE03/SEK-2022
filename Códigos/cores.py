from time import sleep,time

s_max_branco = 0.05
v_min_branco = 0.70
v_max_preto = 0.3
v_min_preto = 0.09
v_max_vazio = 0.03

#vermelho = (5, 0.8612, 0.8196) 
#azul = (210.0, 70.0, 50.0)
#amarelo = (40.0, 0.8588, 0.998)

#valores hsv [min, max]
tol = 10 #tolerancia
verde = [(129.45521739130436-tol), (149.37876169271863+tol)]
vermelho = [(3.2142622452083978+0.01), (357.65651924181503-tol)]
azul = [(200.6094768214075-tol), (208.5861669649437+tol)]
amarelo = [(21.436035990750977-tol), (32.76189563095437+tol)]
branco = [(0.00390625-0.001),(0.03604910714285714+0.0001+0.1)] #valores de saturacao no caso do branco


class Cores():

    def __init__(self, snr):
        self.snr = snr
        self.rgbmax = self.definir_rgbmax()
        print(self.rgbmax)

    def definir_rgbmax(self): #snr = [sensor_cor_direito, sensor_cor_esquerdo]
        sleep(2)
        rgbmax = []
        for sensor in self.snr:
            rgbmax.append([sensor.red,sensor.green,sensor.blue])
        if 0 in rgbmax[0] or 0 in rgbmax[1]:
            self.definir_rgbmax()
        return rgbmax

    
    def cor(self, sensor):
        old = time()
        if sensor =='esq':     
            snr = self.snr[1]
            rgb_max = self.rgbmax[1]

        else:
            snr = self.snr[0]
            rgb_max = self.rgbmax[0]
        
        rgb_cru1 = [snr.red,snr.green,snr.blue]
        sleep(0.01)
        rgb_cru2 = [snr.red,snr.green,snr.blue]
        sleep(0.01)
        rgb_cru3 = [snr.red,snr.green,snr.blue]

        rgb_cru = [0,0,0]
        for i in range(3):
            rgb_cru[i]=(rgb_cru1[i]+rgb_cru2[i]+rgb_cru3[i])/3

        rgb = self.escalarRGB(rgb_cru,rgb_max)               
        hsv = self.RGBtoHSV(rgb)       
        if (rgb_cru[0]<9 and rgb_cru[1]<9 and rgb_cru[2]<9) or hsv[2]<v_max_vazio:
            return 0 #'vazio'
        elif hsv[1] > branco[0] and hsv[1] < branco[1]:
            return 6 #'branco'
        elif hsv[0] > verde[0] and hsv[0] < verde[1]:
            return 3 #verde
        elif hsv[0] < vermelho[0] or hsv[0] > vermelho[1]:
            return 5 #'vermelho'
        elif hsv[0] > azul[0] and hsv[0] < azul[1]:
            return 2 #'azul'
        elif hsv[0] > amarelo[0] and hsv[0] < amarelo[1]:
            return 4 #'amarelo'
        elif hsv[2] < v_max_preto and hsv[2] > v_min_preto:
            return 1 #'preto'
        else:
            return 6
    
    def RGBtoHSV(self, rgb):
        x = max(rgb)
        y = min(rgb)
        if x==y:
            z = 1
        else:
            z = x-y
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        if r>=g and r>=b: #se o vermelho é o máximo
            if g>=b:
                h = 60*(g-b)/z
            else:
                h = 360 + (60*(g-b)/z)
        elif g>=r and g>=b: # se verde é o máximo
            h = 120 + (60*(b-r)/z)
        else:
            h = 240 + (60*(r-g)/z)
        s = z/(x+1)
        v = x/255
        hsv_lido = [h,s,v]

        return hsv_lido

    def escalarRGB(self, rgb_in, rgb_max):

        while 0 in rgb_max: self.definir_rgbmax()
        try:
            rcor = 255.0*rgb_in[0]/rgb_max[0]
            gcor = 255.0*rgb_in[1]/rgb_max[1]
            bcor = 255.0*rgb_in[2]/rgb_max[2]
        except:
            self.definir_rgbmax()
            rcor = 255.0*rgb_in[0]/rgb_max[0]
            gcor = 255.0*rgb_in[1]/rgb_max[1]
            bcor = 255.0*rgb_in[2]/rgb_max[2]

        # print(rcor)
        # print(gcor)
        # print(bcor)
        rgb_cor = [rcor,gcor,bcor]


        for i in range(0,3):
            if rgb_cor[i] > 255:
                rgb_cor[i] = 255
            if rgb_cor[i] < 0:
                rgb_cor[i] = 0
    
        return rgb_cor

    def get_hsv(self,sensor):
        if sensor =='esq':     
            snr = self.snr[1]
            rgb_max = self.rgbmax[1]

        else:
            snr = self.snr[0]
            rgb_max = self.rgbmax[0]
        
        rgb_cru1 = [snr.red,snr.green,snr.blue]
        sleep(0.05)
        rgb_cru2 = [snr.red,snr.green,snr.blue]
        sleep(0.05)
        rgb_cru3 = [snr.red,snr.green,snr.blue]

        rgb_cru = [0,0,0]
        for i in range(3):
            rgb_cru[i]=(rgb_cru1[i]+rgb_cru2[i]+rgb_cru3[i])/3

        rgb = self.escalarRGB(rgb_cru,rgb_max)               
        hsv = self.RGBtoHSV(rgb)  
        return hsv