import plugin_template
import RPi.GPIO as GPIO
import time

class gpio(plugin_template.plugin):

    pwms = {}

    def __init__(self):
        print("plugin gpio constructor")
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setmode(GPIO.BCM)
        
    def __del__(self):
        GPIO.cleanup()
        
    def get_data(self, url):
        args = url.split('/')
        channel = int(args[2])
        mode = args[3]
        #action["off"] = self.set_gpio
        #action[mode](channel, GPIO.LOW)
        
        if mode == "off":
            self.set_gpio(channel, GPIO.LOW)
        elif mode == "on":
            self.set_gpio(channel, GPIO.HIGH)
        elif mode == "get":
            return self.get_gpio(channel)
        elif mode == "pwm":
            cycle = args[4]
            self.change_pwm(channel, cycle)
        return args

    def set_data(self):
        raise Exception("not implemented")

    ##
    # GPIO.INPUT,
    # GPIO.OUTPUT
    # GPIO.SPI, GPIO.I2C, GPIO.HARD_PWM, GPIO.SERIAL ou GPIO.UNKNOWN.
    #
    def get_direction(self, channel):
        return GPIO.gpio_function(channel)

    ##
    # GPIO.HIGH | GPIO.LOW 
    def set_gpio(self, channel, state):
        GPIO.setup(channel, GPIO.OUT) 
        GPIO.output(channel, state)

    def get_gpio(self, channel, state):
        GPIO.setup(channel, GPIO.IN) 
        GPIO.input(channel, state)

    def register_pwm(self, channel):
        GPIO.setup(channel, GPIO.OUT)
        pwm = GPIO.PWM(channel, 500)
        pwm.start(100)
        self.pwms[channel] = pwm
        return pwm

    def change_pwm(self, channel, cycle):
        pwm = self.get_pwm(channel)
        cycle = float(cycle) % 100
        pwm.ChangeDutyCycle(cycle)

    def get_pwm(self, channel):
        if self.pwms.has_key(channel):
            pwm = self.pwms[channel]
        else:
            pwm = self.register_pwm(channel)
        return pwm
        
