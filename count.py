import os
import glob
from tkinter import *
from tkinter import ttk
root = Tk()

basePath = os.path.abspath(".")
ignore = ["venv"]
def getFolders(path=None):
    if path == None:path = basePath
    return [x for x in os.listdir(path) if os.path.isdir(x) and x not in ignore]

def listFiles(path):
    f= [z for x in os.walk(path) for z in x[-1]]
    return f

def renamePath(new,old,path):
    _old = os.path.join(path,old)
    _new = os.path.join(path,new)
    os.rename(_old,_new)

def main():
    dirs = getFolders()
    Dirs = {}
    for d in dirs:
        files = listFiles(os.path.join(basePath,d))
        Dirs[d]=len(files)
        renamePath(f"[{len(files)}] {d}",d,basePath)
    progress = ttk.Progressbar(root, orient = HORIZONTAL, length = 120)

if __name__ =="__main__":
    main()