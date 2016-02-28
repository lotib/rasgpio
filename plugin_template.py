
class plugin:
    
    def __init__(self):
        print "plugin template constructor"

    def get_data(self, url):
        raise Exception("not implemented")

    def set_data(self):
        raise Exception("not implemented")

    def get_name(self):
        return self.__class__.__name__
    

