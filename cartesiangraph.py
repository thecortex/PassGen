from custom import CHARSLIST
from multiprocessing import Process
import os

def customgen(password, outputfilename="temp.txt", outwidget=None):
    vecs = []
    for chr in password:
        if chr == "?":
            vecs.append(CHARSLIST)
        else:
            vecs.append([chr])
    with open(outputfilename, 'a') as f:
        recursive_aux(vecs, 0, "", f, outwidget)
    f.close()
    return

def recursive_aux(vecs, idx, sofar, filehdl, outwidget=None):
    if idx >= len(vecs):
        outwidget.append(sofar)
        filehdl.write('\n\r%s'%sofar)
        return
    for letter in vecs[idx]:
        # info('main line')
        # p = Process(target=recursive_aux, args=(vecs, idx+1, sofar + letter, filehdl, outwidget))
        # p.start()
    # p.join()
        recursive_aux(vecs, idx+1, sofar + letter, filehdl, outwidget)
    return

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()