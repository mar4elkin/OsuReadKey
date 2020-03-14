class Core(object):

    def __init__(self, c=''):
        self.c = c

    def windowsKeyReader(self):
        import msvcrt

        num = 0
        done = False
        while not done:
            print(num)
            num += 1

            if msvcrt.kbhit():
                print ("you pressed",msvcrt.getch(),"so now i will quit")
                done = True

    def linuxKeyReader(self):
        pass

    def macOSKeyReader(self):
        pass

        