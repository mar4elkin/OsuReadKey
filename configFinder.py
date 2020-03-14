import glob, os
from osPaths import OsPaths

osSelector = OsPaths()
selecters = osSelector.detectOs()

class ConfigFinder(object):

    def __init__(self, configs=''):
        self.configs = configs
    
    def findConfig(self):
        self.configs = []

        os.chdir(selecters[1])
        for file in glob.glob("*.ocon"):
            self.configs.append(file)

        return self.configs

