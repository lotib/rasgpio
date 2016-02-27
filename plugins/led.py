import plugin_template

print "led"

class led(plugin_template.plugin):
    
    def __init__(self):
        print "plugin led constructor"
        plugin_template.plugin.__init__(self)
        print "plugin led constructor"


    def get_data(self):
        raise Exception("not implemented")

    def set_data(self):
        raise Exception("not implemented")

    def get_name(self):
        return "plugin led"
