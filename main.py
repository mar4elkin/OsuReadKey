from configWorker import ConfigWorker
from configFinder import ConfigFinder

if __name__ == '__main__':
    finder = ConfigFinder()
    configs = finder.findConfig()
    worker = ConfigWorker(configs)

    if (configs != []):
        #use it in programm
        selectedConfig = worker.selectConfig()
    else:
        worker.createConfig()
        selectedConfig = worker.selectConfig()
        



