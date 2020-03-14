import sys
import os
from sys import platform

class OsPaths(object):
    
    def __init__(self, c=''):
        self.c = c
    
    def detectOs(self):
        userOS = None
        if platform == "linux" or platform == "linux2":
            print('Sorry, but linux x is unsupposed right now')
            userOS = 'linux'
            sys.exit(0)

        elif platform == "darwin":
            userOS = 'macOS'
            desktopPath = os.path.join(os.path.join(os.environ['HOME']), 'Desktop')
            homePath = desktopPath + '/' + 'osureadkey'
            return desktopPath, homePath, userOS
            
        elif platform == "win32":
            userOS = 'win32'
            desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            homePath = desktopPath + '\\' + 'osureadkey'
            return desktopPath, homePath, userOS