import plugin_template

import RPi.GPIO as GPIO
import time


class gpio:
    
    def __init__(self):
        print "plugin template constructor"

    def __del__(self):
        GPIO.cleanup()
    
        
    def get_data(self, url):

        args = url.split('/')
        
        return args 
        
        raise Exception("not implemented")

    def set_data(self):
        raise Exception("not implemented")

    def get_name(self):
        return "plugin template"

    ##
    # GPIO.INPUT,
    # GPIO.OUTPUT
    # GPIO.SPI, GPIO.I2C, GPIO.HARD_PWM, GPIO.SERIAL ou GPIO.UNKNOWN.
    #
    def get_direction(channel):
        return GPIO.gpio_function(channel)

    ##
    # GPIO.HIGH | GPIO.LOW 
    def set_gpio(channel, state):
        GPIO.setup(channel, GPIO.OUT) 
        GPIO.output(channel, state)

    def get_gpio(channel, state):
        GPIO.setup(channel, GPIO.IN) 
        GPIO.input(channel, state)

    
