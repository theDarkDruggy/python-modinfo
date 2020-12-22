import sys
sys.path.append("../../funcs")
import funcs
import linecache

modules = []
classes = []
##### GETTING FUNCTIONS #####
FuncsInmod = funcs.getFuncsInmod(linecache,"linecache")
FuncsInclass = []
#####=====#####
##### CHOOSING #####
info = """
The linecache module allows one to get any line from a Python source
file, while attempting to optimize internally, using a cache, the common
case where many lines are read from a single file. This is used by the
traceback module to retrieve source lines for inclusion in the formatted
traceback.
"""
funcs.printInfo(info)
funcs.getChoose(modules,classes,FuncsInmod,FuncsInclass)
#####=====#####
