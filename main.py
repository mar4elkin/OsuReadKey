from configWorker import ConfigWorker
from configFinder import ConfigFinder

if __name__ == '__main__':
    finder = ConfigFinder()
    worker = ConfigWorker()
    configs = finder.findConfig()

    if (configs != []):
        #use it in programm
        selectedConfig = worker.selectConfig(configs)
    else:
        pass
        



# import msvcrt

# num = 0
# done = False
# while not done:
#     print(num)
#     num += 1

#     if msvcrt.kbhit():
#         print ("you pressed",msvcrt.getch(),"so now i will quit")
#         done = True