import os
from pathlib import Path

class ConfigWorker(object):
    
    def __init__(self, fConfigs='', toReadKeys=''):
        self.fConfigs = fConfigs
        self.toReadKeys = toReadKeys

    def selectConfig(self):
        for config in len(self.fConfigs):
            print(config)

        print('To select config, type config name')
        selConfig = str(input()) + '.ocon'

        for i in self.fConfigs:
            if(selConfig == self.fConfigs[i]):
                return self.fConfigs[i]
            
        

    def writeToConfig(self, desktopPath, homePath, config_name):
        configFile = open(homePath + '\\' + config_name + ".ocon","w+")

        print('type keys and seperate it with comma')
        
        keys = input()
        keysArr = keys.replace(' ', '').split(',')

        for i in range(len(keysArr)):
            configFile.write(keysArr[i]+'\n')

    def createConfig(self):
        crConfigName = True
        desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        homePath = desktopPath + '\\' + 'osureadkey'

        print('Config will be saved to ' + homePath)

        while(crConfigName):
            
            print('Type config name')
            configName = str(input())

            if (configName != ''):
                if (Path(homePath).mkdir(parents=True, exist_ok=True)):
                    crConfigName = False    
                    configFile = open(homePath + '\\' + configName + ".ocon","w+")
                    self.writeToConfig(desktopPath, homePath, configName)
                else:
                    try:
                        f = open(homePath + '\\' + configName + ".ocon")
                        f.close()
                        print('Config already created')
                    except FileNotFoundError:
                        crConfigName = False   
                        configFile = open(homePath + '\\' + configName + ".ocon","w+")
                        self.writeToConfig(desktopPath, homePath, configName)
            else: 
                print("Config name can't be empty")
