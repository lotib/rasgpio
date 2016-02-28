#!/usr/bin/python3

import imp
from os import listdir
from os.path import isfile, join
import inspect
import signal, os

PLUGIN_PATH="plugins"

plugins = {}


def register_signals():
        signal.signal(signal.SIGINT, handler)
        signal.signal(signal.SIGTERM, handler)


def load_plugins():
        plugin_files = [f for f in listdir(PLUGIN_PATH) if isfile("{}/{}".format(PLUGIN_PATH, f)) and f.endswith(".py")]        
        for f in plugin_files:
                plugin_module = imp.load_source(PLUGIN_PATH, "{}/{}".format(PLUGIN_PATH, f))
                for name, obj in inspect.getmembers(plugin_module):                        
                        if inspect.isclass(obj):

                                print('starting plugin', name, 'from', f)

                                plugin_obj = obj()
                                plugins[plugin_obj.get_name()] = plugin_obj


def unload_plugins():
        for key, plugin in plugins.iteritems():
                del plugin
        
def handler(signum, frame):
        unload_plugins()
        print('Signal handler called with signal', signum)
        exit()

load_plugins()
