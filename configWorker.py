#stock libs
import os
from pathlib import Path
#core
from osPaths import OsPaths
from core import Core

coreK = Core()
osSelector = OsPaths()
selecters = osSelector.detectOs()

class ConfigWorker(object):
    
    def __init__(self, fConfigs):
        self.fConfigs = fConfigs

    def selectConfig(self):
        print('select config or create another one\n'
        + 'to create new config type create')
        if (str(input()) == 'create'):
            self.createConfig()
        else: 
            for i in range(0, len(self.fConfigs)):
                print(self.fConfigs[i])

        print('To select config, type config name')
        selConfig = str(input()+'.ocon') 

        for i in range(len(self.fConfigs)):
            if(selConfig == self.fConfigs[i]):
                # return self.fConfigs[i] 
                self.readConfig(self.fConfigs[i])
    
    def readConfig(self, config_name):
        if (selecters[2] == 'win32'):
            configFile = open(selecters[1] + '\\' + config_name, "r")
            configList = configFile.readlines()
            configFile.close()
            configListClear = []
            for i in range(len(configList)):
                configListClear.append(configList[i].replace('\n', ''))
            #print(configListClear)
            coreK.windowsKeyReader(configListClear)

        elif (selecters[2] == 'linux'):
            configFile = open(selecters[1] + '/' + config_name, "r")
            coreK.linuxKeyReader()

        elif (selecters[2] == 'macOS'):
            configFile = open(selecters[1] + '/' + config_name, "r")
            coreK.macOSKeyReader()


    def writeToConfig(self, config_name):
        configFile = open(selecters[1] + '\\' + config_name + ".ocon","w+")

        print('type keys and seperate it with comma')
        
        keys = input()
        keysArr = keys.replace(' ', '').split(',')

        for i in range(len(keysArr)):
            configFile.write(keysArr[i]+'\n')

    def createConfig(self):
        crConfigName = True

        print('Config will be saved to ' + selecters[1])

        while(crConfigName):
            
            print('Type config name')
            configName = str(input())

            if (configName != ''):
                if (Path(selecters[1]).mkdir(parents=True, exist_ok=True)):
                    crConfigName = False    
                    if (selecters[2] == 'win32'):
                        configFile = open(selecters[1] + '\\' + configName + ".ocon","w+")

                    elif (selecters[2] == 'linux'):
                        configFile = open(selecters[1] + '/' + configName + ".ocon","w+")

                    elif (selecters[2] == 'macOS'):
                        configFile = open(selecters[1] + '/' + configName + ".ocon","w+")

                    self.writeToConfig(configName)
                else:
                    try:
                        if (selecters[2] == 'win32'):
                            f = open(selecters[1] + '\\' + configName + ".ocon")

                        elif (selecters[2] == 'linux'):
                            f = open(selecters[1] + '/' + configName + ".ocon")

                        elif (selecters[2] == 'macOS'):
                            f = open(selecters[1] + '/' + configName + ".ocon")

                        f.close()
                        print('Config already created')
                    except FileNotFoundError:
                        crConfigName = False   
                        
                        if (selecters[2] == 'win32'):
                            configFile = open(selecters[1] + '\\' + configName + ".ocon","w+")

                        elif (selecters[2] == 'linux'):
                            configFile = open(selecters[1] + '/' + configName + ".ocon","w+")

                        elif (selecters[2] == 'macOS'):
                            configFile = open(selecters[1] + '/' + configName + ".ocon","w+")

                        self.writeToConfig(configName)
            else: 
                print("Config name can't be empty")
