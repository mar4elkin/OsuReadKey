import glob, os

class ConfigFinder(object):

    def __init__(self, configs=''):
        self.configs = configs
    
    def findConfig(self):
        self.configs = []
        desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        homePath = desktopPath + '\\' + 'osureadkey'

        os.chdir(homePath)
        for file in glob.glob("*.ocon"):
            self.configs.append(file)

        return self.configs

