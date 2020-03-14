class Core(object):

    def __init__(self, c=''):
        self.c = c

    #def saveScore():

    def windowsKeyReader(self, config):
        import msvcrt
        done = False
        print('to stop programm type: *')
        print('to erase data type: !')

        keyDict = { }

        for key in range(len(config)):
            keyDict[config[key]] = 0

        while not done:
            if (msvcrt.kbhit()):
                key = str(msvcrt.getch()).replace("b", "").replace("'", "")

                if (key in config):
                    val = keyDict.get(key, "")
                    keyDict[key] = val+1
                    print(keyDict)

                if (key == '*'):
                    done = True

                if (key == '!'):
                    keyDict = { }
                    for key in range(len(config)):
                        keyDict[config[key]] = 0
                    print(keyDict)

    def linuxKeyReader(self):
        pass

    def macOSKeyReader(self):
        pass

        