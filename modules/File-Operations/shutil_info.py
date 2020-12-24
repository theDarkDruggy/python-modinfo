import sys
sys.path.append("../../funcs")
import funcs
import shutil

##### GETTING MODULES #####
modules = []
#####=====#####
##### GETTING CLASSES #####
classes = funcs.getClasses(shutil,"shutil")
#####=====#####
##### GETTING FUNCTIONS #####
FuncsInmod = funcs.getFuncsInmod(shutil,"shutil")
FuncsInclass = (funcs.getFuncsInclass(shutil._GiveupOnFastCopy,"shutil._GiveupOnFileCopy")+
                funcs.getFuncsInclass(shutil._ntuple_diskusage,"shutil._ntuple_diskusage"))
#####=====#####
##### CHOOSING #####
info = """
The shutil module offers a number of high-level operations on files and collections
of files. In particular, functions are provided which support file copying and
removal. For operations on individual files, see also the os module.
"""
funcs.printInfo(info)
funcs.getChoose(modules,classes,FuncsInmod,FuncsInclass)
#####=====#####
