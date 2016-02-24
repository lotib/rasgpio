import sys

class plugin:
    
    def __init__(self):
        print "plugin default constructor"

    def get_data(self):
        raise Exception("not implemented")

    def set_data(self):
        raise Exception("not implemented")

    def get_name(self):
        return "plugin sample"
    
