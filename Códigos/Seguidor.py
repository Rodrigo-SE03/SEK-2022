class colorPID:

    reflected_target = 60
    power = 15
    kp = 1; ki = 0.0; kd = 0

    def __init__(self, sensor,vel = 30):
        self.sensor = sensor
        self.integral = 0
        self.last_error = 0
        self.power = vel
    
    def get_error(self): return self.reflected_target - self.sensor.reflected_light_intensity

    def get_integral(self, error):
        self.integral += error
        return self.integral

    def get_derivative(self, error):
        derivative = error - self.last_error
        self.last_error = error
        return derivative
    
    def PID(self):
        error = self.get_error()
        integral = self.get_integral(error)
        derivative = self.get_derivative(error)
        return ((error*self.kp) + (integral*self.ki) + (derivative*self.kd))
    
    def reset(self):
        self.integral = 0
        self.last_error = 0
